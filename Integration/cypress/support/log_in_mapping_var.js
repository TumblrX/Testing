/** 
 * first div that contain two buttons, second sign up botton
 * @const BEGIN_LOG_IN */
const BEGIN_LOG_IN = '.MainPage_login__27tt_'
/** 
 * inside input tag in sign up form
 * @const INPUT_EMAIL  */
const INPUT_EMAIL = '[data-testid="email"]'
/** 
 * inside input tag in sign up form
 * @const INPUT_PASSWORD */
const INPUT_PASSWORD = '[data-testid="password"]'
/**
 * first div that contain form, second button
 *  @const LOG_IN_ACTION */
const LOG_IN_ACTION = '[data-testid="login"]'
/** 
 * first div that contain form, second div contain error message
 * @const ERROR_MSG_EMPTY_DATA */
const ERROR_MSG_EMPTY_DATA = '[data-testid="emptyData"]'
/** 
* first div that contain form, second div contain error message
* @const ERROR_MSG_EMPTY_EMAIL */
const ERROR_MSG_EMPTY_EMAIL = '[data-testid="emptyEmail"]'
/** 
* first div that contain form, second div contain error message
* @const ERROR_MSG_EMPTY_PASSWORD */
const ERROR_MSG_EMPTY_PASSWORD = '[data-testid="emptyPassword"]'
/** 
* first div that contain form, second div contain error message
* @const ERROR_MSG_WRONG_DATA */
const ERROR_MSG_WRONG_DATA = '[data-testid="wrongData"]'

 /** @const */const VARIABLES = {
    BEGIN_LOG_IN: BEGIN_LOG_IN, INPUT_EMAIL: INPUT_EMAIL, INPUT_PASSWORD: INPUT_PASSWORD,
    LOG_IN_ACTION: LOG_IN_ACTION, ERROR_MSG_EMPTY_DATA: ERROR_MSG_EMPTY_DATA, ERROR_MSG_EMPTY_EMAIL: ERROR_MSG_EMPTY_EMAIL,
    ERROR_MSG_EMPTY_PASSWORD: ERROR_MSG_EMPTY_PASSWORD, ERROR_MSG_WRONG_DATA: ERROR_MSG_WRONG_DATA
}
module.exports = { VARIABLES }
