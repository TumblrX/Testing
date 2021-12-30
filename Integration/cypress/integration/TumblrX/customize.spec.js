/// <reference types="cypress" />

const { CUSTOMIZE_VARIABLES } = require("../../support/customize_mapping_var")
import {signIn,customizeIconClicked,changeTitle,changeDescription,changeHeaderImage,changeAvatarSquare,changeAvatarCircle,changeBackground,changeTitleColor,showImageHeader} from '../../support/customize_func'


describe("Edit appearance",function(){
 
    // sign in into tumblr
    it("sign in",function(){
        signIn(CUSTOMIZE_VARIABLES.password,CUSTOMIZE_VARIABLES.email)
    })

    // Go to customize from the search bar icon
    it("get edit appearance icon clicked",function(){
        customizeIconClicked()
    })
    // cahnge title of user page 
    it("change title",function(){
        changeTitle("Mennaa")
    })
    // change description
    it("change description ",function(){
        changeDescription("BUTTERFLIES IMPACT NEVER LOST!!")
    })
    // change header image
    it("change header image ",function(){
        changeHeaderImage()
    })
    // change avatar to square shape
    it("change avatar to square shape ",function(){
        changeAvatarSquare()
    })
    // change avatar to circle shape
    it("change avatar to circle shape ",function(){
        changeAvatarCircle()
    })
    // change background color
    it("change background color ",function(){
        changeBackground()
    })
    // change title color
    it("change Title color ",function(){
        changeTitleColor()
    })
    // toggle show image header
    it("Toggle show image header",function(){
        showImageHeader()
    })
})
