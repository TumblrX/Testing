// ***********************************************
// This example commands.js shows you how to
// create various custom commands and overwrite
// existing commands.
//
// For more comprehensive examples of custom
// commands please read more here:
// https://on.cypress.io/custom-commands
// ***********************************************
//
//
// -- This is a parent command --
// Cypress.Commands.add('login', (email, password) => { ... })
//
//
// -- This is a child command --
// Cypress.Commands.add('drag', { prevSubject: 'element'}, (subject, options) => { ... })
//
//
// -- This is a dual command --
// Cypress.Commands.add('dismiss', { prevSubject: 'optional'}, (subject, options) => { ... })
//
//
// -- This will overwrite an existing command --
// Cypress.Commands.overwrite('visit', (originalFn, url, options) => { ... })
import 'cypress-iframe';
import { workingSignUp } from './sign_up_func';
import { workingLogIn } from './log_in_func';

/**
 * this function allow us to test the ideal case for sign in
 */
Cypress.Commands.add('workingSignUp', function () {
    workingSignUp()
})
/**
 * this function allow us to test the ideal case for log in
 */
Cypress.Commands.add('workingLogIn', function () {
    workingLogIn()
})
