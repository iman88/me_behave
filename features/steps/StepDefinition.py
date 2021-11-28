import behave

@behave.given(u'I navigate to "{url}"}')
def step_impl(context, url):
    context.driver.get(url)

@behave.given(u'User is on Registration page')
def step_impl(context):
    context.driver.get('https://thetestingworld.com/index.php?option=com_users&view=registration&Itemid=588')

@behave.when(u'User enters username')
def step_impl(context):
    context.driver.find_element_by_id('jform_name').send_keys('Abcd')

@behave.when(u'User enters email id')
def step_impl(context):
    context.driver.find_element_by_id('jform_email1').send_keys('abc@abc.com')

@behave.when(u'User enters password')
def step_impl(context):
    context.driver.find_element_by_id('jform_password1').send_keys('Welcome123!')

@behave.when(u'User clicks on signup button')
def step_impl(context):
    context.driver.find_element_by_xpath('//button[@type="submit"]').click()

@behave.then(u'The user should be registered successfully')
def step_impl(context):
    print("Registered")
