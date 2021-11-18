/// <reference types="cypress" />

// (describe) function is used to hold a collection of tests 
// and (it) function represents an individual test
describe("login",function(){
    it("sign in",function(){

        cy.visit('https://www.tumblr.com/')
        cy.get('.Fygd5 .Z8Ux2').contains('Log in').click({force: true})
        cy.get('input[name="email"]').type("mennaahmedali77@gmail.com").should("be.visible")
        cy.get('input[name="password"]').type("menna").should("be.visible")
        cy.get('.EvhBA').contains('Log in').click({force: true})
        
    })
    
    it("Add Quote",function(){

        

        
    })
    // it("Create Text post",function(){

        
    //     cy.get('.FOqaP').contains('Text').click({force: true})
    //     cy.waitFor(5000)
    //     cy.get('.control').click({force: true})
    //     // cy.get('editor').find('p').type("This post was created by a test script ")
    //     // // cy.get('.root').find('p').type("This post was created by a test script ")
    //     // cy.get('.button-area').contains('Post').click()

        
    // })

})
