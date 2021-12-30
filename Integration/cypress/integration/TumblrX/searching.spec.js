/// <reference types="cypress" />

import { placeholderExistance, searchAndRoutes, goToTagRoute, goToBlogRoute, tsettTagPage, tsetSearchPage } from'../../support/searching_func'
import { WEB_URL } from '../../url'

describe('Searching', () => {
  beforeEach(() => {
    cy.visit(WEB_URL)
    cy.workingLogIn()
  })
  it("is there placeholder", function () {
    placeholderExistance('Search Tumblr')
  })
  it("test empty search", function () {
    searchAndRoutes("", '/explore/recommended-for-you')
    //-- tsetExplorePage()
  })
  it("test only spaces", function () {
    searchAndRoutes(" ", '/explore/')
    //-- tsetExplorePage() 
  })
  it("test text with spaces in", function () {
    searchAndRoutes("nada   1111111a", '/search/nada1111111a')
    tsetSearchPage("nada 1111111a")
  })
  it("knowen word", function () {
    searchAndRoutes("test", "/search/test")
    tsetSearchPage("test")
  })

})
