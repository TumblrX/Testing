/// <reference types="cypress" />

import { checkFollowing } from'../../support/following_func'

describe('Message', () => {
  beforeEach(() => {
    cy.visit('http://tumblrx.me:4000/') //http://tumblrx.me:4000/dashboard
    cy.workingLogIn()
  })
  it("is there placeholder", function () {
    checkFollowing()
  })
})
