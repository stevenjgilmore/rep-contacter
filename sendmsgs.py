import settings

from mechanize import Browser


def msgthomtillis(send=True):

    br = Browser()

    # Ignore robots.txt
    br.set_handle_robots(False)
    # Google demands a user-agent that isn't a robot
    br.addheaders = [('User-agent', 'Firefox')]
    br.open("https://www.tillis.senate.gov/public/index.cfm/email-me")

    br.form = list(br.forms())[1]  # use when form is unnamed

    control = br.form.find_control("field_700BE99B-C12A-4836-BD02-D87FCD7ADECD")
    control.value = [settings.prefix]
    control = br.form.find_control("field_554EB441-1332-47D8-B817-87A030531FCC")
    control.value = settings.first
    control = br.form.find_control("field_77689247-ECBE-4E25-97D6-62F8A979E226")
    control.value = settings.last
    control = br.form.find_control("field_47F809FC-8DE7-4768-95BE-6B94DCC7C8C8")
    control.value = settings.address
    control = br.form.find_control("field_CE57ACC9-B469-40E7-8C69-CD582376C1BB")
    try:
        control.value = settings.address2
    except Exception:
        pass
    control = br.form.find_control("field_965E8165-21F8-49A4-AAD0-E72A361EC2DB")
    control.value = settings.city
    control = br.form.find_control("field_575CA444-CC6F-441A-BB35-41F458536AD0")
    try:
        control.value = [settings.state]
    except Exception:
        control.value = ['NC']
    control = br.form.find_control("field_F35EA2FD-C92A-4FFC-9CE0-637B8AEECB54")
    control.value = settings.zipcode
    control = br.form.find_control("field_64322B9D-7F15-47DA-B656-9843D7D04866")
    control.value = settings.phone
    control = br.form.find_control("field_5C0C729A-D702-46F1-9821-7DD7E565E136")
    control.value = settings.email
    control = br.form.find_control("field_957A77F6-59C6-4500-8A3B-9AE76484F733")
    control.value = [settings.topic]
    control = br.form.find_control("field_E2D2548D-F3B7-48F7-9BD0-E29F4ED82A43")
    control.value = settings.subject
    control = br.form.find_control("field_279EFB03-F78D-4924-8599-F04AEB99A7A6")
    control.value = settings.msg
    control = br.form.find_control("field_D44885AF-4F13-49FB-A1A7-1F19DDC104FA")
    control.value = ['0']

    if send==True:
        response = br.submit()
        print response.read()
        return response
    return br.form


