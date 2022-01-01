import { VARIABLES } from './message_mapping_var';
import './commands'

/**
 * this function allow us to send a message
 * @param {string}           msg           word that will send to friend.
 */
export function sendMsg(msg) {
    msg = msg 
    cy.get(VARIABLES.TEXT_AREA).type(msg + "{enter}")
    cy.get(VARIABLES.LAST_MSG_ID).find('div').eq(-1).should('contain', msg)
}
/**
 * this function allow us to send a message to friend.
 * @param {string}           msg           word that will send to friend.
 */
 export function sendMsgForFriend(msg) {
    cy.get(VARIABLES.MESSAGE_ICON).find('span').eq(0).click()
    cy.get(VARIABLES.CHAT_FRIEND).eq(0).click({ force: true })
    sendMsg(msg)
}
/**
 * this function allow us to send a message to new friend.
 * @param {string}           name           name of new frind to chat with.
 * @param {string}           msg            word that will send to friend.
 */
 export function sendMsgForNewFriend(name, msg) {
    cy.get(VARIABLES.MESSAGE_ICON).find('span').eq(0).click()
    cy.get(VARIABLES.NEW_MESSAGE).find('span').eq(1).click()
    cy.get(VARIABLES.SEARCHING_FOR_NEW_FRIEND).type(name)
    cy.get(VARIABLES.TO_SEND_BUTTON).find('div').eq(0).click()
    cy.get(VARIABLES.CHAT_FRIEND).find('div').eq(1).contains(name).click()
    sendMsg(msg)
}
/**
 * this function allow us to go to sound settings and test route
 */
export function tsetSoundSettingRoute() {
    cy.get(VARIABLES.MESSAGE_ICON).find('span').eq(0).click()
    cy.get(VARIABLES.CHAT_FRIEND).eq(0).click({ force: true })
    cy.get(VARIABLES.MESSAGE_ICON).find('span').eq(0).click()
    cy.get(VARIABLES.MORE_SETTINGS).click({ force: true })
    cy.get(VARIABLES.SOUND_SETTINGS).find('li').eq(0).click({ force: true })
    cy.url().should('include', 'settings/account')
}
/**
 * this function allow us to change password and other parameter will be ideal
 * @param {string}           word           tha word which we are searching about.
 */
export function tsetDeleteConversation() {
    cy.get(VARIABLES.MESSAGE_ICON).find('span').eq(0).click()
    cy.get(VARIABLES.CHAT_FRIEND).eq(0).click({ force: true })
    cy.get(VARIABLES.MESSAGE_ICON).find('span').eq(0).click()
    cy.get(VARIABLES.MORE_SETTINGS).click({ force: true })
    cy.get(VARIABLES.DELETE_CONVERSATION).find('li').eq(1).click({ force: true })
    cy.get(VARIABLES.LAST_MSG_ID).should('not.exist')
}
