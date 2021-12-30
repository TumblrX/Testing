
import { VARIABLES } from './searching_mapping_var';

/**
 * this function allow us to check placeholder
 */
export function placeholderExistance(placeholder) {
    cy.get(VARIABLES.SEARCH_INPUT).invoke('attr', 'placeholder').should('contain', placeholder)
}
/**
 * this function allow us to submit search string and check the route for search action
 * @param {string}           word           word that will search for.
 * @param {string}           route          the route that expected.
 */
export function searchAndRoutes(word, route) {
    word = word + "{enter}"
    cy.get(VARIABLES.SEARCH_INPUT).type(word)
    cy.url().should('include', route)
}

/**
 * this function allow us to change password and other parameter will be ideal
 * @param {string}           word           tha word which we are searching about.
 */
export function tsetSearchPage(word) {
    cy.get(VARIABLES.SEARCH_WORD_IN_SEARCH_PAGE).contains(word)
    if (find(VARIABLES.POST_ID).length > 0) {
        cy.get(VARIABLES.POST_ID).contains(word)
    }else{
        cy.log('there is no results')
    }
}
