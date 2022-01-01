
import { VARIABLES } from './searching_mapping_var';

/**
 * this function allow us to check placeholder
 */
export function placeholderExistance() {
    cy.get(VARIABLES.SEARCH_INPUT).invoke('attr', 'placeholder').should('contain', 'Search Tumblr')
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
 * this function allow us to submit search string and check the route for Go TO # action
 * @param {string}           word           word that will search for.
 * @param {string}           route          the route that expected.
 */
 export function goToTagRoute(word, route) {
    cy.get(VARIABLES.SEARCH_INPUT).type(word)
    cy.get(VARIABLES.GO_TO_TAG).first().contains(word).click()
    cy.url().should('include', route)
}
/**
 * this function allow us to submit search string and check the route for Go TO @ action
 * @param {string}           word           word that will search for.
 * @param {string}           route          the route that expected.
 */
 export function goToBlogRoute(word, route) {
    cy.get(VARIABLES.SEARCH_INPUT).type(word)
    cy.get(VARIABLES.GO_TO_BLOG).last().contains(word).click()
    cy.url().should('include', route)
}
/**
 * this function allow us to change password and other parameter will be ideal
 * @param {string}           word           tha word which we are searching about.
 */
export function tsettTagPage(word) {
    cy.get(VARIABLES.TAG_DIV).contains(word)
}
/**
 * this function allow us to change password and other parameter will be ideal
 * @param {string}           word           tha word which we are searching about.
 */
export function tsetSearchPage(word) {
    cy.get(VARIABLES.SEARCH_WORD_IN_SEARCH_PAGE).contains(word)
}
