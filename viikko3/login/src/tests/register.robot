*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  tom
    Set Password  tom12345
    Set Password confirmation  tom12345
    Click  button >> text=Register
    Register Should Succeed


Register With Too Short Username And Valid Password
    Set Username  hi
    Set Password  12345678
    Set Password confirmation  12345678
    Click  button >> text=Register
    Register Should Fail With Message  Username should be atleast 3 symbols long

Register With Valid Username And Too Short Password
    Set Username  pete 
    Set Password  123
    Set Password confirmation  123
    Click  button >> text=Register
    Register Should Fail With Message  Password should be atleast 8 symbols long

Register With Username That Is Already In Use
    Set Username  max
    Set Password  distinct
    Set Password confirmation  distinct
    Click  button >> text=Register
    Register Should Fail With Message  Username is already in use

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Get Text  body  *=  ${message}

Set Password confirmation
    [Arguments]  ${password_confirmation}
    Fill Secret  id=password_confirmation  $password_confirmation

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  max  max12345
    Go To Register Page