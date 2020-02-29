# selenium drivers
import json
import re
import socket
import time, datetime
from urllib.parse import urlparse

import xlsxwriter
from RPAPanel.forms import NodesForm, HubsForm
from RPAPanel.models import BotUploadedFiles, Apps, Nodes, Hubs, BotApsTrackingBranch, BotErrorLogs
from RPAPanel.models import HhflBankStatements, query_getfileviews_by_args, query_apps_by_args, query_nodes_by_args, \
    query_hubs_by_args
from RPAPanel.serializers import TimelineSerializer, UpdateSerializer, FiledataSerializer, AppSerializer, \
    NodeSerializer, HubSerializer, BotSerializer, \
    TrackSerializer, CompleteSerializer, ErrorSerializer
from django.contrib import messages
from django.db import connections, OperationalError
from django.db.models import Q
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
# Create your views here.
from rest_framework import viewsets, status
# Create your views here.
# Node View
from rest_framework.response import Response
from rest_framework.utils import json
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from collections import namedtuple

Timeline = namedtuple('Timeline', ('list1', 'list2'))

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# import xlwt
# from xlwt import Workbook

# end

db_conn = connections['datacapture_db']
try:
    c = db_conn.cursor()
except OperationalError:
    connected = False
else:
    connected = True

curs = db_conn.cursor()


def indexapps(request):
    html = TemplateResponse(request, 'apps/index.html')
    return HttpResponse(html.render())


def addapps(request):
    return render(request, "apps/add.html")


def editapps(request, id):
    apps = Apps.objects.get(id=id)
    return render(request, "apps/edit.html", {'apps': apps})


def index(request):
    html = TemplateResponse(request, 'nodes/index.html')
    return HttpResponse(html.render())


def addnode(request):
    return render(request, "nodes/add.html")


def edit(request, id):
    nodes = Nodes.objects.get(id=id)
    return render(request, 'nodes/edit.html', {'nodes': nodes})


def edithubs(request, id):
    hubs = Hubs.objects.get(id=id)
    return render(request, 'hubs/edit.html', {'hubs': hubs})


def addprocess(request):
    if request.method == 'POST':
        form = NodesForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                # messages.success(request, 'Successfully Added')
                # return redirect('/Nodes')
                # response = {'status': 1, 'message': _("Ok")}
                return HttpResponse(json.dumps(Response), content_type='application/json')
            except:
                pass
        else:
            messages.error(request, form.errors)
    else:
        form = NodesForm()
    return render(request, "process/add.html", {'form': form})


# Create your views here.
class AppViewSet(viewsets.ModelViewSet):
    queryset = Apps.objects.all()
    serializer_class = AppSerializer

    def list(self, request, **kwargs):
        try:
            users = query_apps_by_args(**request.query_params)
            serializer = AppSerializer(users['items'], many=True)
            result = dict()
            result['data'] = serializer.data
            result['draw'] = users['draw']
            result['recordsTotal'] = users['total']
            result['recordsFiltered'] = users['count']
            return Response(result, status=status.HTTP_200_OK, template_name=None, content_type=None)

        except Exception as e:
            return Response(str(e), status=status.HTTP_404_NOT_FOUND, template_name=None, content_type=None)


class NodeViewSet(viewsets.ModelViewSet):
    queryset = Nodes.objects.all()
    serializer_class = NodeSerializer

    def list(self, request, **kwargs):
        try:
            users = query_nodes_by_args(**request.query_params)
            serializer = NodeSerializer(users['items'], many=True)
            result = dict()
            result['data'] = serializer.data
            result['draw'] = users['draw']
            result['recordsTotal'] = users['total']
            result['recordsFiltered'] = users['count']
            return Response(result, status=status.HTTP_200_OK, template_name=None, content_type=None)

        except Exception as e:
            return Response(e, status=status.HTTP_404_NOT_FOUND, template_name=None, content_type=None)


# Hub View
def indexhub(request):
    html = TemplateResponse(request, 'hubs/index.html')
    return HttpResponse(html.render())


class HubViewSet(viewsets.ModelViewSet):
    queryset = Hubs.objects.all()
    serializer_class = HubSerializer

    def list(self, request, **kwargs):
        try:
            users = query_hubs_by_args(**request.query_params)
            serializer = HubSerializer(users['items'], many=True)
            result = dict()
            result['data'] = serializer.data
            result['draw'] = users['draw']
            result['recordsTotal'] = users['total']
            result['recordsFiltered'] = users['count']
            return Response(result, status=status.HTTP_200_OK, template_name=None, content_type=None)

        except Exception as e:
            return Response(e, status=status.HTTP_404_NOT_FOUND, template_name=None, content_type=None)


def addhub(request):
    if request.method == 'POST':
        form = HubsForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                # messages.success(request, 'Successfully Added')
                return redirect('/Nodes')
                # response = {'status': 1, 'message': _("Ok")}
                # return HttpResponse(json.dumps(response), content_type='application/json')
            except:
                pass
        else:
            messages.error(request, form.errors)
    else:
        form = HubsForm()
    return render(request, "hubs/add.html", {'form': form})


# Process View
def indexprocess(request):
    html = TemplateResponse(request, 'process/index.html')
    return HttpResponse(html.render())


# Process View
def indexdatacapture(request):
    # return HttpResponse(request.POST)
    # aps_list = request.POST['apps_list']
    aps_list = request.POST.get('apps_list')
    # return HttpResponse(len(aps_list))
    # aps_list = aps_list.split(",")
    # for app_no in apps_list:
    #     return HttpResponse(app_no)
    # return HttpResponse(request)

    # if len(aps_list) > 0:
    if not aps_list:
        html = TemplateResponse(request, 'datacapture/index.html')
        return HttpResponse(html.render())
    else:
        aps_list = aps_list.split(",")
        # aps_list = request.POST['apps_list']
        # apps_list = aps_list.split(",")
        # for app_no in apps_list:
        #     return HttpResponse(app_no)
        # #     return HttpResponse(app_no)
        try:
            # chromObj = webdriver.Remote(
            #     command_executor='http://localhost:4445/wd/hub',
            #     desired_capabilities=DesiredCapabilities.CHROME)
            chromObj = webdriver.Chrome(
                "C:\\Users\\30175\\PycharmProjects\\BCCL_automation\\Remote Selenium\\chromedriver.exe")
            chromObj.get("https://idisburse.icicibank.com:447/idecisions/ilogin")
            chromObj.set_window_size(1250, 917)
            chromObj.find_element(By.ID, "username").click()
            chromObj.find_element(By.ID, "username").send_keys("VARAPL1")
            chromObj.find_element(By.ID, "password").send_keys("VARA@123")
            dropdown = chromObj.find_element(By.ID, "apsOdUserType")
            dropdown.find_element(By.XPATH, "//option[. = 'Vendor']").click()
            chromObj.find_element(By.ID, "SUBMIT").click()
            time.sleep(5)
            chromObj.switch_to.frame(1)
            chromObj.find_element(By.NAME, "userLoginView").click()
            chromObj.find_element(By.NAME, "userLoginView").send_keys("VARAPL1")
            chromObj.find_element(By.NAME, "userPasswordView").send_keys("VARA@123")
            chromObj.find_element(By.CSS_SELECTOR, "tr:nth-child(5) .BUTTONENABLED:nth-child(1)").click()
            chromObj.switch_to.alert.accept()
            chromObj.find_element(By.NAME, "btnProductSaveDetails").click()
            time.sleep(2)
            # self.vars["window_handles"] = chromObj.window_handles
            # time.sleep(5)
            # size = len(self.vars["window_handles"])
            # return HttpResponse(size)
            # chromObj.switch_to.frame(chromObj.find_element(By.ID,"APS"))
            chromObj.switch_to.frame(chromObj.find_element(By.NAME, "banner"))
            chromObj.find_element(By.NAME, "selBranch").click()
            dropdown = chromObj.find_element(By.NAME, "selBranch")
            time.sleep(2)
            # dropdown.find_element(By.XPATH, "//option[. = 'HYDERABAD-P']").click()
            # dropdown.selectByValue('53037');
            chromObj.find_element_by_xpath("//select[@name='selBranch']/option[text()='HYDERABAD-P']").click()
            time.sleep(2)
            # chromObj.find_element(By.NAME, "selBranch").click()
            chromObj.switch_to.alert.accept()
            chromObj.switch_to.default_content()
            # chromObj.switch_to.frame(1)
            chromObj.switch_to.frame(chromObj.find_element(By.ID, "APS"))
            chromObj.switch_to.frame(chromObj.find_element(By.NAME, "contents"))
            chromObj.find_element(By.ID, "ntTree10d").click()
            time.sleep(2)
            chromObj.find_element(By.ID, "ntTree11d").click()
            time.sleep(2)
            chromObj.find_element(By.ID, "ntTree122d").click()
            wh_now = chromObj.window_handles
            chromObj.switch_to_window(wh_now[1])
            time.sleep(2)
            txtAppFormNo = ""
            for app_no in aps_list:
                txtAppFormNo = app_no
                # chromObj.find_element(By.NAME, "txtAppId").click()
                # chromObj.find_element(By.NAME, "txtAppId").send_keys("789456123")
                # app_field = chromObj.find_element(By.NAME, "txtAppFormNo")
                # app_field.clear()
                app_field = chromObj.find_element(By.NAME, "txtAppId")
                app_field.clear()
                # chromObj.find_element(By.NAME, "txtAppFormNo").send_keys(app_no)
                app_field.send_keys(app_no)
                time.sleep(1)
                chromObj.find_element(By.NAME, "btnSearch").click()
                time.sleep(1)
                try:
                    branch_row = chromObj.find_element_by_xpath('/html/body/form/table[4]/tbody/tr[2]/td[2]')
                    branch_name = branch_row.text
                    curs.execute("SELECT branch_code from plbranch_master where branch_desc='" + branch_name + "'")
                    branch_code = curs.fetchone()
                    sql = "UPDATE bot_aps_tracking SET branch_name = '" + str(branch_name) + "', branch = '" + str(
                        branch_code[0]) + "', status = '1'  WHERE apsNo = '" + str(app_no) + "'"
                    row = curs.execute(sql)
                except NoSuchElementException as exception:
                    add_exception(exception, txtAppFormNo)
                    continue
                time.sleep(1)
            chromObj.close()
            chromObj.switch_to_window(wh_now[0])
            chromObj.close()
            return HttpResponse(1)
        except NoSuchElementException as exception:
            add_exception(exception, txtAppFormNo)
            return HttpResponse(exception)
    # else:
    #     return HttpResponse(3333333333)
    #     return HttpResponse(0)

    html = TemplateResponse(request, 'datacapture/index.html')
    return HttpResponse(html.render())


def startDataCapture(request):
    aps_list = request.POST.get('apsno')
    # return HttpResponse(aps_list)
    # for app_no in aps_list:
    #     return HttpResponse(app_no)
    # return HttpResponse(request)
    ip = request.META.get('REMOTE_ADDR')
    hostname = socket.gethostname()
    if not aps_list:
        html = TemplateResponse(request, 'datacapture/index.html')
        return HttpResponse(html.render())
    else:
        aps_list = aps_list.split(",")
        # chromObj = webdriver.Remote(
        #     # command_executor='http://localhost:4445/wd/hub',
        #     command_executor='http://' + ip + ':8001/wd/hub',
        #     desired_capabilities=DesiredCapabilities.CHROME)

        # sql = 'INSERT INTO nodes (name, ip, port) values("' + hostname + '","' + ip + '","1234")'
        # curs.execute(sql)

        # chromObj = webdriver.Remote(
        # command_executor='\\\\10.1.29.220:4445\\wd\\hub',
        # desired_capabilities=DesiredCapabilities.CHROME)
        # chromObj = webdriver.Remote(new URL("http://127.0.0.1:4445",DesiredCapabilities.CHROME))

        chromObj = webdriver.Chrome("C:\\Users\\30175\\PycharmProjects\\BCCL_automation\\Remote "
                                    "Selenium\\chromedriver.exe")
        chromObj.get("https://idisburse.icicibank.com:447/idecisions/ilogin")
        chromObj.set_window_size(1250, 917)
        chromObj.find_element(By.ID, "username").click()
        chromObj.find_element(By.ID, "username").send_keys("VARAPL1")
        chromObj.find_element(By.ID, "password").send_keys("VARA@123")
        dropdown = chromObj.find_element(By.ID, "apsOdUserType")
        dropdown.find_element(By.XPATH, "//option[. = 'Vendor']").click()
        chromObj.find_element(By.ID, "SUBMIT").click()
        time.sleep(2)
        chromObj.switch_to.frame(1)
        chromObj.find_element(By.NAME, "userLoginView").click()
        chromObj.find_element(By.NAME, "userLoginView").send_keys("VARAPL1")
        chromObj.find_element(By.NAME, "userPasswordView").send_keys("VARA@123")
        chromObj.find_element(By.CSS_SELECTOR, "tr:nth-child(5) .BUTTONENABLED:nth-child(1)").click()
        time.sleep(5)
        chromObj.switch_to.alert.accept()
        chromObj.find_element(By.NAME, "btnProductSaveDetails").click()
        time.sleep(2)

        chromObj.switch_to.frame(chromObj.find_element(By.NAME, "banner"))
        chromObj.find_element(By.NAME, "selBranch").click()
        dropdown = chromObj.find_element(By.NAME, "selBranch")
        time.sleep(2)
        # dropdown.find_element(By.XPATH, "//option[. = 'HYDERABAD-P']").click()
        # dropdown.selectByValue('53037');
        chromObj.find_element_by_xpath("//select[@name='selBranch']/option[text()='HYDERABAD-P']").click()
        time.sleep(1)
        chromObj.switch_to.alert.accept()
        for app in aps_list:
            try:
                aps_no = app
                curs.execute("SELECT branch from bot_aps_tracking where apsNo='" + aps_no + "'")
                branch_code = curs.fetchone()
                time.sleep(1)

                curs.execute("SELECT status FROM pldataentry WHERE apsNo = '" + aps_no + "'")
                statusarray = curs.fetchall()
                promo_code = ""
                employer_code = ""
                dmecode = ""
                if len(statusarray) == 0:
                    chromObj.get(
                        "https://aps.icicibank.com/ICICIWeb/Activity.los?activity=BDE&currentActivity=BDE"
                        "&txtApplicationNo=" + str(
                            aps_no) + "&category=PERSONAL&mode=V&inBranchID=" + str(branch_code[0]))
                    time.sleep(2)
                    promo_code = chromObj.find_element(By.NAME, "selFirstSourceType").get_attribute("value")
                    employer_code = chromObj.find_element(By.NAME, "txtEmployerCode").get_attribute("value")
                    dmecode = chromObj.find_element(By.NAME, "txtOSPId").get_attribute("value")
                time.sleep(1)
                if len(statusarray) > 0:
                    chromObj.get(
                        "https://aps.icicibank.com/ICICIWeb/Activity.los?activity=BDE&currentActivity=BDE"
                        "&txtApplicationNo=" + str(
                            aps_no) + "&category=HOME&mode=E&inBranchID=" + str(branch_code[0]))

                chromObj.get(
                    "https://aps.icicibank.com/ICICIWeb/Applicant.los?applicationStatus=&activity=BDE&currentActivity"
                    "=UND&activityEdit=E&hidIsLink=Y&tabKey=APPLICANT&pageName=Applicant.los?applicationStatus"
                    "=&activity=BDE&currentActivity=UND&activityEdit=E&hidIsLink=Y")
                time.sleep(3)
                # data = chromObj.page_source
                # dropdown.find_element(By.XPATH, "//option[. = 'Vendor']").click()
                # elementcnt = len(hromObj.find_elements_by_xpath('//*[@name="applicantAF"]/table[8]/tbody/tr[n]'))
                # return HttpResponse(elementcnt)
                table_id = chromObj.find_element(By.XPATH, '//*[@name="applicantAF"]/table[8]')
                elementcnt = len(table_id.find_elements(By.TAG_NAME, "tr"))
                if elementcnt > 0:
                    elementcnt = elementcnt + 1
                    for i in range(1, elementcnt):
                        if i == 1 or i == 2:
                            continue
                        if len(statusarray) != 0 and ("P" in statusarray) and i == '3':
                            continue
                        if len(statusarray) != 0 and ("C1" in statusarray) and i == '4':
                            continue
                        if len(statusarray) != 0 and ("C2" in statusarray) and i == '5':
                            continue
                        if len(statusarray) != 0 and ("C3" in statusarray) and i == '6':
                            continue
                        if len(statusarray) != 0 and ("C4" in statusarray) and i == '7':
                            continue

                        if i != '1':
                            chromObj.get(
                                "https://aps.icicibank.com/ICICIWeb/Applicant.los?applicationStatus=&activity=BDE"
                                "&currentActivity=UND&activityEdit=E&hidIsLink=Y&tabKey=APPLICANT&pageName=Applicant"
                                ".los?applicationStatus=&activity=BDE&currentActivity=UND&activityEdit=E&hidIsLink=Y")
                        time.sleep(1)
                        # return HttpResponse(111111111)

                        custDtl = chromObj.find_element_by_xpath(
                            "/html/body/form/table[8]/tbody/tr[" + str(i) + "]/td[2]/a").get_attribute("onclick")
                        regex = r"([^']+)"
                        matches = re.findall(regex, custDtl)

                        if (matches[1]):
                            url = matches[1]
                            parts = urlparse(url)
                            query = parts.query
                            query_str = (query.split('&'))
                            custId = (query_str[6].split('='))
                            custId = custId[1]

                        if i != '3':
                            cocount = i - 3
                        chromObj.get(
                            "https://aps.icicibank.com/ICICIWeb/PersonalDetailsOld.los?displayFlag=P&showLowerTab=T"
                            "&pageName=PersonalDetailsOld.los&tabKey=APPLICANT&currentActivity=BDE&activity=BDE"
                            "&hidCustomerID=" + custId + "&ComingFrom=APPLIST&hidGCDCustomerID=")

                        firstname = chromObj.find_element(By.NAME, "txtFName").get_attribute("value")
                        middlename = chromObj.find_element(By.NAME, "txtMName").get_attribute("value")
                        lastname = chromObj.find_element(By.NAME, "txtLName").get_attribute("value")
                        app_dob = chromObj.find_element(By.NAME, "txtDob").get_attribute("value")
                        qualification = chromObj.find_element(By.NAME, "selEduQualification").get_attribute("value")
                        gender = chromObj.find_element(By.NAME, "selSex").get_attribute("value")
                        maritalStatus = chromObj.find_element(By.NAME, "selMaritalStatus").get_attribute("value")
                        accomodationCat = chromObj.find_element(By.NAME, "selAccomodationCategory").get_attribute(
                            "value")
                        # return HttpResponse(aps_list)
                        chromObj.get(
                            "https://aps.icicibank.com/ICICIWeb/PersonalInfo.los?Action=OtherPersonalDetails&CustId=" + custId + "&ApplicantType=P&GCDCustId=&currentActivity=BDE")
                        time.sleep(1)
                        motherMname = chromObj.find_element(By.NAME, "txtMotherFName").get_attribute("value")
                        fatherName = chromObj.find_element(By.NAME, "txtFatherName").get_attribute("value")
                        pan_no = chromObj.find_element(By.NAME, "txtPanNo").get_attribute("value")
                        adhar_no = chromObj.find_element(By.NAME, "txtAdharNo").get_attribute("value")
                        spouseName = chromObj.find_element(By.NAME, "txtSpouseName").get_attribute("value")
                        spouseDob = chromObj.find_element(By.NAME, "txtSpouseDOB").get_attribute("value")
                        resi_type = chromObj.find_element(By.NAME, "selResidentType").get_attribute("value")

                        chromObj.get(
                            "https://aps.icicibank.com/ICICIWeb/Address.los?displayFlag=P&showLowerTab=T&pageName"
                            "=Address.los&tabKey=APPLICANT&currentActivity=BDE&activity=BDE&hidCustomerID=" + custId
                            + "&ComingFrom=APPLIST&hidGCDCustomerID=")
                        time.sleep(1)

                        # ressi address

                        custDtl = chromObj.find_element_by_xpath(
                            "/html/body/form/table[10]/tbody/tr[2]/td[2]/a").click()

                        r_address1 = chromObj.find_element(By.NAME, "txtAddressOne").get_attribute("value")
                        r_address2 = chromObj.find_element(By.NAME, "txtAddressTwo").get_attribute("value")
                        r_address3 = chromObj.find_element(By.NAME, "txtAddressThree").get_attribute("value")
                        r_address4 = chromObj.find_element(By.NAME, "txtAddressFour").get_attribute("value")
                        r_mobileno = chromObj.find_element(By.NAME, "txtMobile").get_attribute("value")
                        r_std = chromObj.find_element(By.NAME, "txtStdisd").get_attribute("value")
                        r_Phone1 = chromObj.find_element(By.NAME, "txtPhoneOne").get_attribute("value")
                        r_Phone2 = chromObj.find_element(By.NAME, "txtPhoneTwo").get_attribute("value")
                        r_email = chromObj.find_element(By.NAME, "txtEmail").get_attribute("value")
                        r_Zip = chromObj.find_element(By.NAME, "txtZip").get_attribute("value")
                        r_City = chromObj.find_element(By.NAME, "txtCity").get_attribute("value")
                        r_State = chromObj.find_element(By.NAME, "selState").get_attribute("value")
                        r_Landmark = chromObj.find_element(By.NAME, "txtLandmark").get_attribute("value")
                        r_Country = chromObj.find_element(By.NAME, "selCountry").get_attribute("value")
                        r_AddYr = chromObj.find_element(By.NAME, "txtAddYear").get_attribute("value")
                        r_AddMon = chromObj.find_element(By.NAME, "txtAddMonth").get_attribute("value")

                        # permanant address

                        custDtl = chromObj.find_element_by_xpath(
                            "/html/body/form/table[10]/tbody/tr[3]/td[2]/a").click()

                        p_address1 = chromObj.find_element(By.NAME, "txtAddressOne").get_attribute("value")
                        p_address2 = chromObj.find_element(By.NAME, "txtAddressTwo").get_attribute("value")
                        p_address3 = chromObj.find_element(By.NAME, "txtAddressThree").get_attribute("value")
                        p_address4 = chromObj.find_element(By.NAME, "txtAddressFour").get_attribute("value")
                        p_mobileno = chromObj.find_element(By.NAME, "txtMobile").get_attribute("value")
                        p_std = chromObj.find_element(By.NAME, "txtStdisd").get_attribute("value")
                        p_Phone1 = chromObj.find_element(By.NAME, "txtPhoneOne").get_attribute("value")
                        p_Phone2 = chromObj.find_element(By.NAME, "txtPhoneTwo").get_attribute("value")
                        p_email = chromObj.find_element(By.NAME, "txtEmail").get_attribute("value")
                        p_Zip = chromObj.find_element(By.NAME, "txtZip").get_attribute("value")
                        p_City = chromObj.find_element(By.NAME, "txtCity").get_attribute("value")
                        p_State = chromObj.find_element(By.NAME, "selState").get_attribute("value")
                        p_Landmark = chromObj.find_element(By.NAME, "txtLandmark").get_attribute("value")
                        p_Country = chromObj.find_element(By.NAME, "selCountry").get_attribute("value")
                        # p_AddYr = chromObj.find_element(By.NAME, "txtAddYear").get_attribute("value")
                        # p_AddMon = chromObj.find_element(By.NAME, "txtAddMonth").get_attribute("value")

                        #  work details
                        chromObj.get(
                            "https://aps.icicibank.com/ICICIWeb/WorkDetail.los?displayFlag=P&showLowerTab=T&pageName=WorkDetail.los&tabKey=APPLICANT&currentActivity=BDE&activity=BDE&hidCustomerID=" + custId + "&ComingFrom=APPLIST&hidGCDCustomerID=")
                        time.sleep(1)

                        empname = chromObj.find_element(By.NAME, "txtSelEmployerID").get_attribute("value")
                        insdustry = chromObj.find_element(By.NAME, "selIndustryID").get_attribute("value")
                        compType = chromObj.find_element(By.NAME, "selConstitutionID").get_attribute("value")
                        workProfession = chromObj.find_element(By.NAME, "selProfession").get_attribute("value")
                        workDesig = chromObj.find_element(By.NAME, "selDesignation").get_attribute("value")
                        workDept = chromObj.find_element(By.NAME, "selDepartment").get_attribute("value")

                        compCurrYear = chromObj.find_element(By.NAME, "txtAddYear").get_attribute("value")
                        compCurrMonth = chromObj.find_element(By.NAME, "txtAddMonth").get_attribute("value")

                        compTotYear = chromObj.find_element(By.NAME, "txtYearInCity").get_attribute("value")
                        compTotMonth = chromObj.find_element(By.NAME, "txtMonthInCity").get_attribute("value")

                        workadd1 = chromObj.find_element(By.NAME, "txtAddressOne").get_attribute("value")
                        workadd2 = chromObj.find_element(By.NAME, "txtAddressTwo").get_attribute("value")
                        workadd3 = chromObj.find_element(By.NAME, "txtAddressThree").get_attribute("value")
                        workadd4 = chromObj.find_element(By.NAME, "txtAddressFour").get_attribute("value")
                        workstd = chromObj.find_element(By.NAME, "txtStdisd").get_attribute("value")
                        workphone1 = chromObj.find_element(By.NAME, "txtPhoneOne").get_attribute("value")
                        workphone2 = chromObj.find_element(By.NAME, "txtPhoneTwo").get_attribute("value")
                        workMob = chromObj.find_element(By.NAME, "txtMobile").get_attribute("value")
                        workemail = chromObj.find_element(By.NAME, "txtEmail").get_attribute("value")
                        workExt = chromObj.find_element(By.NAME, "txtExtension").get_attribute("value")
                        workstate = chromObj.find_element(By.NAME, "selState").get_attribute("value")
                        workcity = chromObj.find_element(By.NAME, "txtCity").get_attribute("value")
                        workCountry = chromObj.find_element(By.NAME, "selCountry").get_attribute("value")
                        workZip = chromObj.find_element(By.NAME, "txtZip").get_attribute("value")
                        workLandmark = chromObj.find_element(By.NAME, "txtLandmark").get_attribute("value")
                        workMailAdd = chromObj.find_element(By.NAME, "selMailingAddress").get_attribute("value")
                        # Income expences

                        chromObj.get(
                            "https://aps.icicibank.com/ICICIWeb/IncomeExpense.los?displayFlag=P&showLowerTab=T&pageName=IncomeExpense.los&tabKey=APPLICANT&currentActivity=BDE&activity=BDE&hidCustomerID=" + custId + "&ComingFrom=APPLIST&hidGCDCustomerID=")

                        try:
                            chromObj.find_element_by_xpath(
                                "//*[@id='tablePersonalIncome3']/tbody/tr[2]/td[2]/a").click()
                            time.sleep(1)
                            netIncome = chromObj.find_element(By.NAME, "txtIncomeTotalAmount").get_attribute("value")
                            netYrIncome = chromObj.find_element(By.NAME, "txtIncomeNetAmount").get_attribute("value")
                            totalYrIncome = chromObj.find_element(By.NAME, "txtIncomeAmount").get_attribute("value")
                        except Exception as e:
                            netIncome = 0
                            netYrIncome = 0
                            totalYrIncome = 0

                            #  bank details
                        chromObj.get(
                            "https://aps.icicibank.com/ICICIWeb/PersonalBank.los?displayFlag=P&showLowerTab=T"
                            "&pageName=PersonalBank.los&tabKey=APPLICANT&currentActivity=BDE&activity=BDE"
                            "&hidCustomerID=" + custId + "&ComingFrom=APPLIST&hidGCDCustomerID=")
                        time.sleep(1)

                        try:
                            chromObj.find_element_by_xpath("/html/body/form/table[10]/tbody/tr[2]/td[2]/a").click()
                            time.sleep(1)

                            bankName = chromObj.find_element(By.NAME, "selBankName").get_attribute("value")
                            bankBranch = chromObj.find_element(By.NAME, "txtBankBranch").get_attribute("value")
                            bankAccNo = chromObj.find_element(By.NAME, "txtAccountNumber").get_attribute("value")
                        except Exception as e:
                            bankName = 0
                            bankBranch = 0
                            bankAccNo = 0

                        #  Reference details

                        chromObj.get(
                            "https://aps.icicibank.com/ICICIWeb/CustRelationRefDetail.los?applicationStatus=&activity=BDE&currentActivity=BDE&activityEdit=V&hidIsLink=Y&tabKey=CUSTRELATIONREF&pageName=CustRelationRefDetail.los?applicationStatus=&activity=BDE&currentActivity=BDE&activityEdit=V&hidIsLink=Y")
                        time.sleep(1)

                        # ref 1

                        chromObj.find_element_by_xpath("/html/body/form/table[10]/tbody/tr[2]/td[2]/a").click()
                        time.sleep(1)

                        ref1_name = chromObj.find_element(By.NAME, "txtReferenceName").get_attribute("value")
                        ref1_rel = chromObj.find_element(By.NAME, "selReferenceRelation").get_attribute("value")
                        ref1_add1 = chromObj.find_element(By.NAME, "txtAddress1").get_attribute("value")
                        ref1_add2 = chromObj.find_element(By.NAME, "txtAddress2").get_attribute("value")
                        ref1_phone1 = chromObj.find_element(By.NAME, "txtPhone1").get_attribute("value")
                        ref1_mob = chromObj.find_element(By.NAME, "txtMobile").get_attribute("value")
                        ref1_city = chromObj.find_element(By.NAME, "txtCity").get_attribute("value")
                        ref1_pin = chromObj.find_element(By.NAME, "txtPin").get_attribute("value")
                        ref1_state = chromObj.find_element(By.NAME, "txtState").get_attribute("value")

                        # ref 2
                        time.sleep(1)

                        chromObj.find_element_by_xpath("/html/body/form/table[10]/tbody/tr[3]/td[2]/a").click()
                        time.sleep(1)
                        ref2_rel = chromObj.find_element(By.NAME, "selReferenceRelation").get_attribute("value")
                        ref2_name = chromObj.find_element(By.NAME, "txtReferenceName").get_attribute("value")
                        ref2_add1 = chromObj.find_element(By.NAME, "txtAddress1").get_attribute("value")
                        ref2_add2 = chromObj.find_element(By.NAME, "txtAddress2").get_attribute("value")
                        ref2_phone1 = chromObj.find_element(By.NAME, "txtPhone1").get_attribute("value")
                        ref2_mob = chromObj.find_element(By.NAME, "txtMobile").get_attribute("value")
                        ref2_city = chromObj.find_element(By.NAME, "txtCity").get_attribute("value")
                        ref2_pin = chromObj.find_element(By.NAME, "txtPin").get_attribute("value")
                        ref2_state = chromObj.find_element(By.NAME, "txtState").get_attribute("value")

                        if (custId):
                            appType = ""
                            if (i == 3):
                                appType = "P"
                            else:
                                var = i - 3
                                appType = "C" + str(var)

                            status = "P"
                            sql = "INSERT INTO pldataentry (applicationNo, apsNo, custid, branch, appType,status, firstname, middlename,lastname,app_dob,qualification,gender,motherMname,fatherName,pan_no,spouseName,spouseDob,resi_type,r_address1,r_address2,r_address3,r_address4,r_mobileno,r_std,r_Phone1,r_Phone2,r_email,r_Zip,r_City,r_State,r_Landmark,r_Country,r_AddYr,r_AddMon,p_address1,p_address2,p_address3,p_address4,p_mobileno,p_std,p_Phone1,p_Phone2,p_email,p_Zip,p_City,p_State,p_Landmark,p_Country,empname,insdustry,compType,workProfession,workDesig,workDept,compCurrYear,compCurrMonth,compTotYear,compTotMonth,workadd1,workadd2,workadd3,workadd4,workstd,workphone1,workphone2,workMob,workExt,workemail,workstate,workcity,workCountry,workZip,workLandmark,workMailAdd,netIncome,netYrIncome,totalYrIncome,bankName,bankBranch,ref1_name,ref1_rel,ref1_add1,ref1_add2,ref1_phone1,ref1_mob,ref1_city,ref1_pin,ref1_state,ref2_name,ref2_rel,ref2_add1,ref2_add2,ref2_phone1,ref2_mob,ref2_city,ref2_pin,ref2_state,promo_code,maritalStatus,adhar_no,accomodationCat,bankAccNo,employer_code,dmecode) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                            val = (
                                str(aps_no), str(aps_no), str(custId), str(branch_code[0]), str(appType), str(status),
                                str(firstname), str(middlename), str(lastname), str(app_dob), str(qualification),
                                str(gender), str(motherMname), str(fatherName), str(pan_no), str(spouseName),
                                str(spouseDob), str(resi_type), str(r_address1), str(r_address2), str(r_address3),
                                str(r_address4), str(r_mobileno), str(r_std), str(r_Phone1), str(r_Phone2),
                                str(r_email),
                                str(r_Zip), str(r_City), str(r_State), str(r_Landmark), str(r_Country), str(r_AddYr),
                                str(r_AddMon), str(p_address1), str(p_address2), str(p_address3), str(p_address4),
                                str(p_mobileno), str(p_std), str(p_Phone1), str(p_Phone2), str(p_email), str(p_Zip),
                                str(p_City), str(p_State), str(p_Landmark), str(p_Country), str(empname),
                                str(insdustry),
                                str(compType), str(workProfession), str(workDesig), str(workDept), str(compCurrYear),
                                str(compCurrMonth), str(compTotYear), str(compTotMonth), str(workadd1), str(workadd2),
                                str(workadd3), str(workadd4), str(workstd), str(workphone1), str(workphone2),
                                str(workMob), str(workExt), str(workemail), str(workstate), str(workcity),
                                str(workCountry), str(workZip), str(workLandmark), str(workMailAdd), str(netIncome),
                                str(netYrIncome), str(totalYrIncome), str(bankName), str(bankBranch), str(ref1_name),
                                str(ref1_rel), str(ref1_add1), str(ref1_add2), str(ref1_phone1), str(ref1_mob),
                                str(ref1_city), str(ref1_pin), str(ref1_state), str(ref2_name), str(ref2_rel),
                                str(ref2_add1), str(ref2_add2), str(ref2_phone1), str(ref2_mob), str(ref2_city),
                                str(ref2_pin), str(ref2_state), str(promo_code), str(maritalStatus), str(adhar_no),
                                str(accomodationCat), str(bankAccNo), str(employer_code), str(dmecode))
                            curs.execute(sql, val)

                        sql = "UPDATE bot_aps_tracking SET status = '2' WHERE apsNo = '" + aps_no + "'"
                        row = curs.execute(sql)
                time.sleep(2)
            except Exception as e:
                add_exception(e, aps_no)
                continue
        # chromObj.close()
        return HttpResponse("Data Capture successfully")


def exportData(request):
    batch_id = request.POST.get('id')
    # return HttpResponse(aps_list)
    # for app_no in aps_list:
    #     return HttpResponse(app_no)
    # return HttpResponse(request)
    if not batch_id:
        html = TemplateResponse(request, 'datacapture/index.html')
        return HttpResponse(html.render())
    else:
        ts = time.time()
        dt_object = datetime.fromtimestamp(ts)
        curr_date = dt_object.strftime("%d_%m_%Y_%H_%M_%S")
        sql = "SELECT \
              de.* \
              FROM pldataentry de \
              INNER JOIN bot_aps_tracking bat ON de.applicationNo = bat.apsNo \
              WHERE bat.batchId = '" + str(batch_id) + "';"
        curs.execute(sql)
        exportData = curs.fetchall()
        if (len(exportData) > 0):
            curs.execute("SELECT file_name FROM bot_uploaded_files WHERE id='" + str(batch_id) + "'")
            file_name = curs.fetchone()
            file_name = file_name[0].split('.')
            # filepath = 'C:\\Users\\54859\\Desktop\\CC_EXCEL\\'+file_name[0]+curr_date+'.xlsx'
            # wb = xlwt.Workbook()
            workbook = xlsxwriter.Workbook('C:\\Users\\54859\\Desktop\\CC_EXCEL\\' + file_name[0] + curr_date + '.xlsx')
            # workbook = xlsxwriter.Workbook('\\\\10.1.21.51\\vara_dev_bpo\\DhananjayPingale\\'+file_name[0]+curr_date+'.xlsx')
            # workbook = xlsxwriter.Workbook('\\\\10.1.31.59\\CCDownloads\\' + file_name[0] + curr_date + '.xlsx')
            worksheet = workbook.add_worksheet()

            row = 0
            col = 0
            worksheet.write(row, col, 'Promo Code')
            worksheet.write(row, col + 1, 'Firstme')
            worksheet.write(row, col + 2, 'Last Name')
            worksheet.write(row, col + 3, 'Mother Maiden Name')
            worksheet.write(row, col + 4, 'Gender')
            worksheet.write(row, col + 5, 'Maritial Status')
            worksheet.write(row, col + 6, 'Educatiol Qalification')
            worksheet.write(row, col + 7, 'Address One')
            worksheet.write(row, col + 8, 'Address Two')
            worksheet.write(row, col + 9, 'Address Three')
            worksheet.write(row, col + 10, 'Address Four')
            worksheet.write(row, col + 11, 'Std code')
            worksheet.write(row, col + 12, 'Phone one')
            worksheet.write(row, col + 13, 'Phone Two')
            worksheet.write(row, col + 14, 'Mobile')
            worksheet.write(row, col + 15, 'Email')
            worksheet.write(row, col + 16, 'Yrs/Mths at current address')
            worksheet.write(row, col + 17, 'Yrs/Mths at current address')
            worksheet.write(row, col + 18, 'Middle Name')
            worksheet.write(row, col + 19, 'Address One')
            worksheet.write(row, col + 20, 'Address Two')
            worksheet.write(row, col + 21, 'Address Three')
            worksheet.write(row, col + 22, 'Father Name')
            worksheet.write(row, col + 23, 'Date of Birth')
            worksheet.write(row, col + 24, 'Address four')
            worksheet.write(row, col + 25, 'Std code')
            worksheet.write(row, col + 26, 'Phone One')
            worksheet.write(row, col + 27, 'Phone Two')
            worksheet.write(row, col + 28, 'Spouse name')
            worksheet.write(row, col + 29, 'Spouse Dob')
            worksheet.write(row, col + 30, 'Mobile')
            worksheet.write(row, col + 31, 'Email')
            worksheet.write(row, col + 32, 'Residence Type')
            worksheet.write(row, col + 33, 'LandMark')
            worksheet.write(row, col + 34, 'Zip')
            worksheet.write(row, col + 35, 'City')
            worksheet.write(row, col + 36, 'State')
            worksheet.write(row, col + 37, 'Accomodation Category')
            worksheet.write(row, col + 38, 'Country')
            worksheet.write(row, col + 39, 'PAN A/C No.')
            worksheet.write(row, col + 40, 'Reference Name')
            worksheet.write(row, col + 41, 'Address one')
            worksheet.write(row, col + 42, 'Address two')
            worksheet.write(row, col + 43, 'Mob')
            worksheet.write(row, col + 44, 'Reference Name 2')
            worksheet.write(row, col + 45, 'LandMark')
            worksheet.write(row, col + 46, 'Pin')
            worksheet.write(row, col + 47, 'city')
            worksheet.write(row, col + 48, 'State')
            worksheet.write(row, col + 49, 'ref Address1')
            worksheet.write(row, col + 50, 'Country')
            worksheet.write(row, col + 51, 'ref Address2')
            worksheet.write(row, col + 52, 'ref Mobile 2')
            worksheet.write(row, col + 53, 'Employer name')
            worksheet.write(row, col + 54, 'Industry')
            worksheet.write(row, col + 55, 'Company Type')
            worksheet.write(row, col + 56, 'Yrs/Mths at current Off/Buss')
            worksheet.write(row, col + 57, 'Yrs/Mths at current Off/Buss')
            worksheet.write(row, col + 58, 'Employer Code')
            worksheet.write(row, col + 59, 'Income Amount')
            worksheet.write(row, col + 60, 'Income Amount')
            worksheet.write(row, col + 61, 'Ref Pincode')
            worksheet.write(row, col + 62, 'Ref 1 City')
            worksheet.write(row, col + 63, 'Ref 1 State')
            worksheet.write(row, col + 64, 'Ref 1 Income Amount')
            worksheet.write(row, col + 65, 'Yrs/Mths at current Off/Buss')
            worksheet.write(row, col + 66, 'Yrs/Mths at current Off/Buss')
            worksheet.write(row, col + 67, 'Ref 2 Pincode')
            worksheet.write(row, col + 68, 'Ref 2 City')
            worksheet.write(row, col + 69, 'Ref 2 state')
            worksheet.write(row, col + 70, 'Total yrs/Mths in Off/Buss')
            worksheet.write(row, col + 71, 'Address one')
            worksheet.write(row, col + 72, 'Occupation')
            worksheet.write(row, col + 73, 'Address two')
            worksheet.write(row, col + 74, 'Address three')
            worksheet.write(row, col + 75, 'Address four')
            worksheet.write(row, col + 76, 'Std code')
            worksheet.write(row, col + 77, 'Phone one')
            worksheet.write(row, col + 78, 'Profession')
            worksheet.write(row, col + 79, 'Phone two')
            worksheet.write(row, col + 80, 'Designation')
            worksheet.write(row, col + 81, 'Ext one')
            worksheet.write(row, col + 82, 'Department')
            worksheet.write(row, col + 83, 'Mobile')
            worksheet.write(row, col + 84, 'Email')
            worksheet.write(row, col + 85, 'Reference Relation/Relationship with Applicant')
            worksheet.write(row, col + 86, 'Account Number')
            worksheet.write(row, col + 87, 'Account Number')
            worksheet.write(row, col + 88, 'Bank Branch')
            worksheet.write(row, col + 89, 'LandMark')
            worksheet.write(row, col + 90, 'Pincode')
            worksheet.write(row, col + 91, 'City')
            worksheet.write(row, col + 92, 'State')
            worksheet.write(row, col + 93, 'Country')
            worksheet.write(row, col + 94, 'Bank Name')
            worksheet.write(row, col + 95, 'Date of Birth')
            worksheet.write(row, col + 96, 'E-UID(Aadhaar)')
            worksheet.write(row, col + 97, 'Mailing address')
            worksheet.write(row, col + 110, 'Aps No')

            row = 1
            col = 0
            # curs.execute("SELECT branch_code from plbranch_master WHERE  branch_desc='"+batch_id+"'")

            # Iterate over the data and write it out row by row.
            i = 0
            for data in exportData:
                worksheet.write(row, col, data[98])
                worksheet.write(row, col + 1, data[12])
                worksheet.write(row, col + 2, data[14])
                worksheet.write(row, col + 2, data[14])
                worksheet.write(row, col + 3, data[8])
                worksheet.write(row, col + 4, data[7])
                worksheet.write(row, col + 5, data[99])  # change marrital status 99
                worksheet.write(row, col + 6, data[6])
                worksheet.write(row, col + 7, data[19])  # address 1
                worksheet.write(row, col + 8, data[20])
                worksheet.write(row, col + 9, data[21])
                worksheet.write(row, col + 10, data[22])  # address 4
                worksheet.write(row, col + 11, data[24])  # std
                worksheet.write(row, col + 12, data[25])
                worksheet.write(row, col + 13, data[26])
                worksheet.write(row, col + 14, data[23])  # mob
                worksheet.write(row, col + 15, data[27])  # email
                worksheet.write(row, col + 16, data[33])  # yr
                worksheet.write(row, col + 17, data[34])  # mon
                worksheet.write(row, col + 18, data[13])  # midd name
                worksheet.write(row, col + 19, data[35])  # add 1
                worksheet.write(row, col + 20, data[36])  # mon
                worksheet.write(row, col + 21, data[37])  # mon
                worksheet.write(row, col + 22, data[15])  # mon  father name
                worksheet.write(row, col + 23, data[5])  # mon dob
                worksheet.write(row, col + 24, data[38])  # mon addres 4
                worksheet.write(row, col + 25, data[40])  # mon std
                worksheet.write(row, col + 26, data[41])  # mon
                worksheet.write(row, col + 27, data[42])  # mon
                worksheet.write(row, col + 28, data[16])  # mon
                worksheet.write(row, col + 29, data[17])  # spouse dob
                worksheet.write(row, col + 30, data[39])  # s per Mobile
                worksheet.write(row, col + 31, data[43])  # per email
                worksheet.write(row, col + 32, data[18])  # Residence Type
                worksheet.write(row, col + 33, data[31])  # curr landmark
                worksheet.write(row, col + 34, data[28])  # curr zip
                worksheet.write(row, col + 35, data[29])  # s City
                worksheet.write(row, col + 36, data[30])  # state
                worksheet.write(row, col + 37, data[101])  # Accomodation Category
                worksheet.write(row, col + 38, data[17])  # r_Country
                worksheet.write(row, col + 39, data[9])  # PAN A/C No.
                worksheet.write(row, col + 40, data[80])  # Reference Name
                worksheet.write(row, col + 41, data[82])  # add 1
                worksheet.write(row, col + 42, data[83])  # add 2
                worksheet.write(row, col + 43, data[85])  # mob
                worksheet.write(row, col + 44, data[89])  # ref name 2
                worksheet.write(row, col + 45, data[47])  # landmark
                worksheet.write(row, col + 46, data[44])  # pin
                worksheet.write(row, col + 47, data[45])  # city
                worksheet.write(row, col + 48, data[46])  # State
                worksheet.write(row, col + 49, data[91])  # ref 2 add1
                worksheet.write(row, col + 50, data[48])  # Country
                worksheet.write(row, col + 51, data[92])  # ref add 2
                worksheet.write(row, col + 52, data[94])  # ref Mobile 2
                worksheet.write(row, col + 53, data[49])  # Employer name
                worksheet.write(row, col + 54, data[50])  # Industry
                worksheet.write(row, col + 55, data[51])  # comp type
                worksheet.write(row, col + 56, data[55])  # curr yr exp
                worksheet.write(row, col + 57, data[56])  # curr month exp
                worksheet.write(row, col + 58, data[103])  # Employer Code
                worksheet.write(row, col + 59, data[77])  # Income
                worksheet.write(row, col + 60, data[75])  # income
                worksheet.write(row, col + 61, data[87])  # REF Pincode
                worksheet.write(row, col + 62, data[86])  # REF Pincode
                worksheet.write(row, col + 63, data[88])  # REF Pincode
                worksheet.write(row, col + 64, data[76])  # Income Amount
                worksheet.write(row, col + 65, data[57])  # Yrs/Mths at current Off/Buss
                worksheet.write(row, col + 66, data[58])  # Yrs/Mths at current Off/Buss
                worksheet.write(row, col + 67, data[96])  # Pincode
                worksheet.write(row, col + 68, data[95])  # City
                worksheet.write(row, col + 69, data[97])  # State
                worksheet.write(row, col + 70, "xxxxxxx")  # Total yrs/Mths in Off/Buss
                worksheet.write(row, col + 71, data[59])  # Address one
                worksheet.write(row, col + 72, "xxxxxxxx")  # Occupation
                worksheet.write(row, col + 73, data[60])  # work Address two
                worksheet.write(row, col + 74, data[61])  # work Address three
                worksheet.write(row, col + 75, data[62])  # work Address four
                worksheet.write(row, col + 76, data[63])  # work Std code
                worksheet.write(row, col + 77, data[64])  # work Phone one
                worksheet.write(row, col + 78, data[52])  # work Profession
                worksheet.write(row, col + 79, data[65])  # work Phone two
                worksheet.write(row, col + 80, data[53])  # work Designation
                worksheet.write(row, col + 81, data[68])  # work Ext one
                worksheet.write(row, col + 82, data[54])  # work Department
                worksheet.write(row, col + 83, data[66])  # Mobile
                worksheet.write(row, col + 84, data[67])  # Email
                worksheet.write(row, col + 85, data[90])  # ref 2rel with app
                worksheet.write(row, col + 86, data[102])  # Account Number
                worksheet.write(row, col + 87, data[102])  # Account Number
                worksheet.write(row, col + 88, data[79])  # Bank Branch
                worksheet.write(row, col + 89, data[73])  # work LandMark
                worksheet.write(row, col + 90, data[72])  # work Pincode
                worksheet.write(row, col + 91, data[70])  # work City
                worksheet.write(row, col + 92, data[69])  # work State
                worksheet.write(row, col + 93, data[71])  # work Country
                worksheet.write(row, col + 94, data[78])  # Bank Name
                worksheet.write(row, col + 95, data[5])  # Date of Birth
                worksheet.write(row, col + 96, data[100])  # E-UID(Aadhaar)
                worksheet.write(row, col + 97, data[74])  # Mailing address
                worksheet.write(row, col + 110, data[1])  # Mailing address
                # sql = "UPDATE bot_aps_tracking SET status = '3' WHERE apsNo = '"+data[2]+"'"
                # row = curs.execute(sql)
                row += 1

            workbook.close()
            for data in exportData:
                sql = "UPDATE bot_aps_tracking SET status = '3' WHERE apsNo = '" + data[2] + "'"
                row = curs.execute(sql)

            if len(exportData):
                sql = "UPDATE bot_uploaded_files SET file_status = '1' WHERE id = '" + str(batch_id) + "'"
                row = curs.execute(sql)
                return HttpResponse(1)
            else:
                sql = "UPDATE bot_uploaded_files SET file_status = '2' WHERE id = '" + str(batch_id) + "'"
                row = curs.execute(sql)
                return HttpResponse(0)
        return HttpResponse("Somthing went wrong.")


def add_exception(exception, txtAppFormNo):
    sql = "INSERT INTO bot_error_logs (exception_dtl, txtAppFormNo ) VALUES (%s,%s)"
    val = (str(exception), str(txtAppFormNo))
    curs.execute(sql, val)
    return HttpResponse(1)


class BotViewSet(viewsets.ModelViewSet):
    queryset = BotApsTrackingBranch.objects.using('datacapture_db').all()
    serializer_class = BotSerializer

    def list(self, request, *args, **kwargs):
        try:
            queryset = BotApsTrackingBranch.objects.using('datacapture_db').filter(Q(status='0') | Q(status='1'))
            total = len(list(queryset))
            draw = int(self.request.query_params.get('draw', None))
            start = int(self.request.query_params.get('start', None))
            length = int(self.request.query_params.get('length', None))
            queryset = queryset[start:start + length]
            serializer = BotSerializer(queryset, many=True)

            result = dict()
            result['data'] = serializer.data
            result['draw'] = draw
            result['recordsTotal'] = total
            result['recordsFiltered'] = total
            return Response(result, status=status.HTTP_200_OK, template_name=None, content_type=None)

        except Exception as e:
            return Response(e, status=status.HTTP_404_NOT_FOUND, template_name=None, content_type=None)


class TrackingViewSet(viewsets.ModelViewSet):
    queryset = BotApsTrackingBranch.objects.using('datacapture_db').all()
    serializer_class = TrackSerializer

    def list(self, request, *args, **kwargs):
        try:
            queryset = BotApsTrackingBranch.objects.using('datacapture_db').filter(bank_stat_id='1')
            total = len(list(queryset))
            draw = int(self.request.query_params.get('draw', None))
            start = int(self.request.query_params.get('start', None))
            length = int(self.request.query_params.get('length', None))
            queryset = queryset[start:start + length]
            serializer = TrackSerializer(queryset, many=True)

            result = dict()
            result['data'] = serializer.data
            result['draw'] = draw
            result['recordsTotal'] = total
            result['recordsFiltered'] = total

            return Response(result, status=status.HTTP_200_OK, template_name=None, content_type=None)

        except Exception as e:
            return Response(e, status=status.HTTP_404_NOT_FOUND, template_name=None, content_type=None)


class TimelineViewSet(viewsets.ViewSet):
    queryset = BotApsTrackingBranch.objects.using('datacapture_db').all()
    serializer_class = TrackSerializer

    def list(self, request):
        timeline = Timeline(
            list1=HhflBankStatements.objects.all(),
            list2=BotApsTrackingBranch.objects.all(),
        )
        serializer = TimelineSerializer(timeline)
        return Response(serializer.data)


class UpdatedataViewSet(viewsets.ModelViewSet):
    queryset = HhflBankStatements.objects.using('datacapture_db').all()
    serializer_class = UpdateSerializer

    def list(self, request, *args, **kwargs):
        if request.method == 'GET':
            queryset = HhflBankStatements.objects.using('datacapture_db').filter(doc_dtl_id=request.GET['appid'])
            serializer = UpdateSerializer(queryset, many=True)

            return Response(serializer.data)

    # def list(self, request, *args, **kwargs):
    #     try:
    #         appid = BotUploadedFiles.objects.get(id=request.data.appid)
    #         return HttpResponse(appid)
    #     except:
    #         return HttpResponse(status=404)


class CompleteViewSet(viewsets.ModelViewSet):
    queryset = BotApsTrackingBranch.objects.using('datacapture_db').all()
    serializer_class = CompleteSerializer

    def list(self, request, *args, **kwargs):
        try:
            queryset = BotApsTrackingBranch.objects.using('datacapture_db').filter(status='3')
            total = len(list(queryset))
            draw = int(self.request.query_params.get('draw', None))
            start = int(self.request.query_params.get('start', None))
            length = int(self.request.query_params.get('length', None))
            queryset = queryset[start:start + length]
            serializer = CompleteSerializer(queryset, many=True)

            result = dict()
            result['data'] = serializer.data
            result['draw'] = draw
            result['recordsTotal'] = total
            result['recordsFiltered'] = total
            return Response(result, status=status.HTTP_200_OK, template_name=None, content_type=None)

        except Exception as e:
            return Response(e, status=status.HTTP_404_NOT_FOUND, template_name=None, content_type=None)


class FileDdataViewSet(viewsets.ModelViewSet):
    queryset = BotUploadedFiles.objects.using('datacapture_db').all()
    serializer_class = FiledataSerializer

    def list(self, request, **kwargs):
        try:
            users = query_getfileviews_by_args(**request.query_params)
            # return Response(users)
            serializer = FiledataSerializer(users['items'], many=True)
            result = dict()
            result['data'] = serializer.data
            result['draw'] = users['draw']
            result['recordsTotal'] = users['total']
            result['recordsFiltered'] = users['count']
            return Response(result, status=status.HTTP_200_OK, template_name=None, content_type=None)

        except Exception as e:
            return Response(e, status=status.HTTP_404_NOT_FOUND, template_name=None, content_type=None)


class ErrorViewSet(viewsets.ModelViewSet):
    queryset = BotErrorLogs.objects.using('datacapture_db').all()
    serializer_class = ErrorSerializer

    def list(self, request, *args, **kwargs):
        try:
            queryset = BotErrorLogs.objects.using('datacapture_db').all()
            total = len(list(queryset))
            draw = int(self.request.query_params.get('draw', None))
            start = int(self.request.query_params.get('start', None))
            length = int(self.request.query_params.get('length', None))
            queryset = queryset[start:start + length]
            serializer = ErrorSerializer(queryset, many=True)

            result = dict()
            result['data'] = serializer.data
            result['draw'] = draw
            result['recordsTotal'] = total
            result['recordsFiltered'] = total
            return Response(result, status=status.HTTP_200_OK, template_name=None, content_type=None)

        except Exception as e:
            return Response(e, status=status.HTTP_404_NOT_FOUND, template_name=None, content_type=None)


def pagedata(request, appid):
    appid = BotUploadedFiles.objects.get(case_id=appid)
    html = TemplateResponse(request, 'datacapture/appdata.html', {'appid': appid})
    return HttpResponse(html.render())
