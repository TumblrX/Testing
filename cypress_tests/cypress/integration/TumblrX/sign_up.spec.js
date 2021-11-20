/// <reference types="cypress" />

import { invalidEmailSignUp, invalidPasswordSignUp, invalidBlogNameSignUp, invalidAgeSignUp } from'../../support/sign_up_func'

describe('Sign Up', () => {
  beforeEach(() => {
    cy.visit('https://www.tumblr.com')
  })
  it("invalid email sign up", function () {
    invalidEmailSignUp("nadaelsayed163@ex", 'That\'s not a valid email address. Please try again.')
  })
  it("empty email sign up", function () {
    invalidEmailSignUp("", 'You forgot to enter your email!')
  })
  it("space in email sign up", function () {
    invalidEmailSignUp(" ", 'Oops. There was an error. Try again.')
  })
  it("taken email sign up", function () {
    invalidEmailSignUp("nada.elsayed01@eng-st.cu.edu.eg", 'This email address is already in use.')
  })
  it("small password sign up", function () {
    invalidPasswordSignUp("1234", 'The password must be at least 8 characters.')
  })
  it("empty password sign up", function () {
    invalidPasswordSignUp("", 'You forgot to enter your password!')
  })
  it("working sign up", function () {
    cy.workingSignUp()
  })
  it("big blog-name sign up", function () {
    invalidBlogNameSignUp("111111111111111111111111111111111", 'That\'s not a valid blog name. Username is too long. Please enter 32 or fewer characters.')
  })
  it("empty blog-name sign up", function () {
    invalidBlogNameSignUp("", 'You forgot to enter your blog name!')
  })
  it("space blog-name sign up", function () {
    invalidBlogNameSignUp(" ", 'Oops. There was an error. Try again.')
  })
  it("char in blog-name sign up", function () {
    invalidBlogNameSignUp("Nada Elsayed", 'That\'s not a valid blog name. Letters, numbers, and dashes only please.')
  })
  it("taken blog-name sign up", function () {
    invalidBlogNameSignUp("Nada-Elsayed-CMP", 'That\'s not a valid blog name. Try something else, that one is spoken for.')  /*That\'s not a valid blog name. Someone beat you to that username. 
                                                                                                                            * That\'s not a valid blog name. That\'s a good one, but it\'s taken.*/
  })
  it("neg age sign up", function () {
    invalidAgeSignUp("-1", 'That\'s not a valid age. Please try again.')
  })
  it("empty age sign up", function () {
    invalidAgeSignUp(" ", 'You forgot to enter your age!')
  })

})
