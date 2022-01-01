/// <reference types="cypress" />

import { invalidEmailLogIn, invalidPasswordLogIn } from'../../support/log_in_func'

describe('Log In', () => {
  beforeEach(() => {
    cy.visit('https://www.tumblr.com')
  })
  it("invalid email log in", function () {
    invalidEmailLogIn("nadaelsayed163@ex", 'Your email or password were incorrect.')
  })
  it("empty email log in", function () {
    invalidEmailLogIn("", 'You forgot to enter your email!')
  })
  it("space in email log in", function () {
    invalidEmailLogIn(" ", 'Your email or password were incorrect.')
  })
  it("false password log in", function () {
    invalidPasswordLogIn("1234", 'Your email or password were incorrect.')
  })
  it("empty password log in", function () {
    invalidPasswordLogIn("", 'You forgot to enter your password!')
  })
  it("working sign up", function () {
    cy.workingLogIn()
  })
})
