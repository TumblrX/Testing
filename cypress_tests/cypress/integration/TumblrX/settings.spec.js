/// <reference types="cypress" />

const { SETTINGS_VARIABLES } = require("../../support/settings_mapping_var")
import {signIn, settingsIconClicked, doesntMatchPasswords, EmptyPasswordAndNoMatch, samePassword, easyGuessed,weakPassword,successfulChange } from '../../support/settings_func'


describe("change settings",function(){
    //sign into tumblr
    it("sign in",function(){

        signIn(SETTINGS_VARIABLES.oldPassword,SETTINGS_VARIABLES.email)
       
    })
    // Go to settings from the search bar icon
    it("get settings icon clicked",function(){
        settingsIconClicked()
    })
    // passwords doesn't match
    it("Passwords don't match",function(){

        doesntMatchPasswords(SETTINGS_VARIABLES.oldPassword,SETTINGS_VARIABLES.weakPassword,SETTINGS_VARIABLES.ALERT_NOMATCH_MESSAGE)
    })
    // passwords doesn't match and empty current password
    it("Empty password and doesn't match",function(){
        EmptyPasswordAndNoMatch(SETTINGS_VARIABLES.oldPassword,SETTINGS_VARIABLES.newPassword,SETTINGS_VARIABLES.ALERT_NOMATCH_MESSAGE,SETTINGS_VARIABLES.ALERT_EMPTY_MESSAGE)
        
    })
    // Same old password
    it("same password",function(){
        samePassword(SETTINGS_VARIABLES.oldPassword,SETTINGS_VARIABLES.oldPassword,SETTINGS_VARIABLES.ALERT_SAMEPASSWORD_MESSAGE)
        
    })
    // Easy to detect passwords
    it("Easy to guess passwords",function(){
        easyGuessed(SETTINGS_VARIABLES.oldPassword,SETTINGS_VARIABLES.easyPassword,SETTINGS_VARIABLES.ALERT_EASYGUESS_MESSAGE)
        
    })
    // less than 8 characters
    it("Weak password",function(){
        weakPassword(SETTINGS_VARIABLES.oldPassword,SETTINGS_VARIABLES.weakPassword,SETTINGS_VARIABLES.ALERT_WEAK_MESSAGE)
        
    })
    //change password successfully
    it("successful change password",function(){
        successfulChange(SETTINGS_VARIABLES.oldPassword,SETTINGS_VARIABLES.newPassword)
    })
})
