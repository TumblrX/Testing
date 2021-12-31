import { HOME_VARIABLES  } from './home_mapping_var';
/**
 * This fnction to sign in
 * @param {string}           password password 
 * @param {string}           email    email.
 */

 export function signIn(password,email,WEB_URL){
   cy.visit(WEB_URL)
   //  cy.visit("https://tumblrx.me")
    cy.get(HOME_VARIABLES.LOGIN_WITH_EMAIL_BUTTON).contains('Log in').click({force: true})
    cy.get(HOME_VARIABLES.INPUT_EMAIL).type(email).should("be.visible")
    cy.get(HOME_VARIABLES.INPUT_PASSWORD).type(password).should("be.visible")
    cy.get(HOME_VARIABLES.LOGIN_BUTTON).contains('Log in').click({force: true})
}
/**
 * This fnction to create Post from home page
 * @param {string}           title post title 
 * @param {string}           text   post text.
 */
 export function addPost(title,text){
    cy.get(HOME_VARIABLES.CREATE_POST_BUTTON).first().click({multiple:true,force:true})
    cy.get(HOME_VARIABLES.POST_TITLE_TEXTBOX).first().type(title)
    cy.get(HOME_VARIABLES.POST_TEXT_TEXTBOX).first().type(text)
    cy.get(HOME_VARIABLES.POST_BUTTON).click({force:true})
    cy.wait(5000)
    cy.reload()
    cy.wait(5000)
    cy.get(HOME_VARIABLES.ADDED_POST_P).should('contain', text)
    
}
/**
 * This fnction to create Post from home page
 */
 export function deletePost(text){
   signIn(HOME_VARIABLES.password,HOME_VARIABLES.email)
   cy.wait(5000)
   cy.get(HOME_VARIABLES.SEARCH_TEXT).click().type(text+"{enter}")
   cy.wait(3000)
   cy.get(HOME_VARIABLES.DELETE_POST_BUTTON).click({multiple:true})
   cy.go('back')
   // problem : Avatar Menna57 button doesn't appear from the test runner
   // cy.get(HOME_VARIABLES.ACCOUNT_ICON).click({multiple:true,force:true})
   // cy.get(HOME_VARIABLES.AVATAR_PAGE_ICON).click({multiple:true,force:true})
}
/**
 * This fnction to like Post from home page
 */
 export function likePost(){
    cy.wait(5000)
    cy.get(HOME_VARIABLES.LIKE_POST_BUTTON).click({multiple:true,force:true})
    cy.wait(3000)
    cy.get(HOME_VARIABLES.CHECK_LIKE_ADDED).invoke('text').then((text1)=>{
       expect(text1).to.eq('1 notes')
    })
    cy.wait(5000)

}
/**
 * This fnction to add comment to a Post from home page
 */
 export function addComment(comment){

    signIn(HOME_VARIABLES.password,HOME_VARIABLES.email)
    cy.wait(3000)
    cy.get(HOME_VARIABLES.ADD_COMMENT_BUTTON).click({force:true,multiple:true})
    cy.get(HOME_VARIABLES.REPLY_TEXTBOX).type(comment)
    cy.wait(3000)
    cy.get(HOME_VARIABLES.REPLY_BUTTON).click({multiple:true,force:true})
    cy.wait(3000)
    cy.get(HOME_VARIABLES.REPLY_BACK_BUTTON).click({multiple:true,force:true})
    cy.get(HOME_VARIABLES.CHECK_LIKE_ADDED).invoke('text').then((text1)=>{
        expect(text1).to.eq('1 notes')
     })

}
/**
 * This fnction to test add Link 
 */
 export function addLink(title,link){

   cy.get(HOME_VARIABLES.CREATE_LINK_BUTTON).click({multiple:true,force:true})
   cy.wait(3000)
   cy.get(HOME_VARIABLES.INSERT_LINK_BUTTON).click()
   cy.get(HOME_VARIABLES.LINK_TITLE).click().type(title)
   cy.get(HOME_VARIABLES.LINK_TARGET).click().type(link)
   cy.get(HOME_VARIABLES.ADD_BUTTON).click({multiple:true,force:true})
   cy.get(HOME_VARIABLES.POST_TITLE_TEXTBOX).first().type(title)
   cy.get(HOME_VARIABLES.POST_TEXT_TEXTBOX).first().click()
   cy.get(HOME_VARIABLES.POST_BUTTON).click({force:true})


}
/**
 * This fnction to test reblog
 */
 export function reblog(){

  cy.get(HOME_VARIABLES.PRE_REBLOG_BUTTON).click({multiple:true})

}

