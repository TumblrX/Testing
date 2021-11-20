/// <reference types="cypress" />

const { settings_variables } = require("../../support/settings_mapping_var")
import {signIn, settingsIconClicked, doesntMatchPasswords, EmptyPasswordAndNoMatch, samePassword, easyGuessed,weakPassword,successfulChange } from '../../support/settings_func'


describe("change settings",function(){
    //sign into tumblr
    it("sign in",function(){

        signIn(settings_variables.old_password,settings_variables.email)
       
    })
    // Go to settings from the search bar icon
    it("get settings icon clicked",function(){
        settingsIconClicked()
    })
    // passwords doesn't match
    it("Passwords don't match",function(){

        doesntMatchPasswords(settings_variables.old_password,settings_variables.weak_password,settings_variables.alert_nomatch_message)
    })
    // passwords doesn't match and empty current password
    it("Empty password and doesn't match",function(){
        EmptyPasswordAndNoMatch(settings_variables.old_password,settings_variables.new_password,settings_variables.alert_nomatch_message,settings_variables.alert_empty_message)
        
    })
    // Same old password
    it("same password",function(){
        samePassword(settings_variables.old_password,settings_variables.old_password,settings_variables.alert_samePassword_message)
        
    })
    // Easy to detect passwords
    it("Easy to guess passwords",function(){
        easyGuessed(settings_variables.old_password,settings_variables.easy_password,settings_variables.alert_easyGuess_message)
        
    })
    // less than 8 characters
    it("Weak password",function(){
        weakPassword(settings_variables.old_password,settings_variables.weak_password,settings_variables.alert_weak_message)
        
    })
    //change password successfully
    it.skip("successful change password",function(){
        successfulChange(settings_variables.old_password,settings_variables.new_password)
    })
})
