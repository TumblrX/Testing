import { CUSTOMIZE_VARIABLES  } from './customize_mapping_var';
import { HOME_VARIABLES  } from './home_mapping_var';
/**
 * This fnction to sign in
 * @param {string}           password password 
 * @param {string}           email    email.
 */

 export function signIn(password,email,WEB_URL){
    // cy.visit(WEB_URL)
    cy.visit("https://tumblrx.me")
    // cy.visit('http://tumblrx.me:4000/') 
    cy.get(HOME_VARIABLES.LOGIN_WITH_EMAIL_BUTTON).contains('Log in').click({force: true})
    cy.get(HOME_VARIABLES.INPUT_EMAIL).type(email).should("be.visible")
    cy.get(HOME_VARIABLES.INPUT_PASSWORD).type(password).should("be.visible")
    cy.get(HOME_VARIABLES.LOGIN_BUTTON).contains('Log in').click({force: true})
}

/**
 * This fnction test open settings from the search bar icon
 */

 export function customizeIconClicked(){
    cy.wait(5000)
    cy.get(CUSTOMIZE_VARIABLES.ACCOUNT_ICON).click({multiple: true})
    cy.get(CUSTOMIZE_VARIABLES.EDIT_APPEARANCE_ICON).click({multiple: true})
}

/**
 * This fnction test change title
 */
 export function changeTitle(newTitle){

    cy.wait(5000)
    cy.get(CUSTOMIZE_VARIABLES.TITLE_TEXTBOX).clear().type(newTitle)
    cy.get(CUSTOMIZE_VARIABLES.SAVE_BUTTON).click()

}

/**
 * This fnction test change description
 */
 export function changeDescription(newDescription){

    cy.wait(5000)
    cy.get(CUSTOMIZE_VARIABLES.DESCRIPTION_TEXTBOX).clear().type(newDescription)
    // cy.get(CUSTOMIZE_VARIABLES.SAVE_BUTTON).click()

}

/**
 * This fnction test change header image 
 */
 export function changeHeaderImage(){
    cy.wait(5000)
    cy.get(CUSTOMIZE_VARIABLES.HEADER_IMAGE_BUTTON).click({multiple: true})
    
}

/**
 * This fnction test change avatar shape
 */
 export function changeAvatarCircle(){

    cy.get(CUSTOMIZE_VARIABLES.AVATAR_CIRCLE_BUTTON).click({multiple: true,force:true})
    cy.wait(2000)
    // cy.get(CUSTOMIZE_VARIABLES.SAVE_BUTTON).click()
    
}
/**
 * This fnction test change avatar shape
 */
 export function changeAvatarSquare(){
    cy.get(CUSTOMIZE_VARIABLES.AVATAR_SQUARE_BUTTON).click({multiple: true,force:true})
    cy.wait(2000)
    cy.get(CUSTOMIZE_VARIABLES.SAVE_BUTTON).click()
    
}
/**
 * This fnction test change background color 
 */
 export function changeBackground(){
    cy.get(CUSTOMIZE_VARIABLES.CHANGE_BACKGROUND_COLOR_BUTTON).invoke('attr', 'value', '#5c3506').should('have.attr', 'value','#5c3506')
    cy.get(CUSTOMIZE_VARIABLES.SAVE_BUTTON).click()
    
}
/**
 * This fnction test change title color 
 */
 export function changeTitleColor(){
    cy.get(CUSTOMIZE_VARIABLES.CHANGE_TITLE_COLOR_BUTTON).invoke('attr', 'value', '#5c3566').should('have.attr', 'value','#5c3566')

    cy.get(CUSTOMIZE_VARIABLES.SAVE_BUTTON).click()
    
}
/**
 * This fnction test show image header
 */
 export function showImageHeader(){
    cy.get(CUSTOMIZE_VARIABLES.TOGGLE_HEADER_IMAGE).click({multiple:true})

    cy.get(CUSTOMIZE_VARIABLES.SAVE_BUTTON).click()
    
}