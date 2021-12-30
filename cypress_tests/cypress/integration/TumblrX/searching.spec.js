/// <reference types="cypress" />

import { placeholderExistance, searchAndRoutes, goToTagRoute, goToBlogRoute, tsettTagPage, tsetSearchPage } from'../../support/searching_func'

describe('Searching', () => {
  beforeEach(() => {
    cy.visit('https://www.tumblr.com')
  })
  it("is there placeholder", function () {
    cy.workingLogIn()
    placeholderExistance()
  })
  it("test empty search", function () {
    cy.workingLogIn()
    searchAndRoutes("", '/explore/recommended-for-you')
    //-- tsetExplorePage()
  })
  it("test only spaces", function () {
    cy.workingLogIn()
    searchAndRoutes(" ", '/explore/')
    //-- tsetExplorePage() 
  })
  it("GO TO #", function () {
    cy.workingLogIn()
    goToTagRoute("nada", '/tagged/nada')
    tsettTagPage("nada")
  })
  it("GO TO @", function () {
    cy.workingLogIn()
    goToBlogRoute("nada", '/blog/view/nada')
    //-- tsetBlogPage("nada")
  })
  it("test text with spaces in", function () {
    cy.workingLogIn()
    searchAndRoutes("nada   1111111a", '/search/nada%20%20%201111111a')
    tsetSearchPage("nada 1111111a")
  })
  // it("unknowen tag", function () {
  //   tsetSearchPage("nada")
  // })
  // it("knowen tag", function () {
  //   tsetSearchPage("nada   1111111a")
  // })

})
