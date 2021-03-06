// /// <reference types="cypress" />

// import { invalidEmailLogIn, invalidPasswordLogIn } from'../../support/log_in_func'
// import { WEB_URL } from '../../url'

// describe('Log In', () => {
//   beforeEach(() => {
//     cy.visit(WEB_URL)
//     cy.visit('http://tumblrx.me:4000/') 
//   })
//   it("invalid email log in", function () {
//     invalidEmailLogIn("nadaelsayed163@ex", 'Your email or password were incorrect.')
//   })
//   it("empty email log in", function () {
//     invalidEmailLogIn("", 'You forgot to enter your email!')
//   })
//   it("space in email log in", function () {
//     invalidEmailLogIn(" ", 'Your email or password were incorrect.')
//   })
//   it("false password log in", function () {
//     invalidPasswordLogIn("1234", 'Your email or password were incorrect.')
//   })
//   it("empty password log in", function () {
//     invalidPasswordLogIn("", 'You forgot to enter your password!')
//   })
//   it("working sign up", function () {
//     cy.workingLogIn()
//   })
// })
