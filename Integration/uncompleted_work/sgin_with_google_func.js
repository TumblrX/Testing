import { VARIABLES } from './sgin_with_google_mapping_var';
import './commands'

/**
 * this function allow us to check placeholder
 */
export function LOG_IN() {
    cy.visit('http://tumblrx.me:4000/', {
        onBeforeLoad(win) {
            cy.stub(win, 'open')
        }
    })

    cy.get(VARIABLES.BEGIN_LOG_IN).contains('Log in').click({ force: true })
    cy.get(VARIABLES.CONTINUE_WITH_GOOGLE_BUTTON_LOG_IN).find('button').click()

    cy.window().its('open').should('be.called')

    cy.get(VARIABLES.MY_EMAIL).click({ force: true })

    // cy.visit("/servicelogin")
    // cy.url().should('contain', 'accounts.google.com')
}
