/** 
 *  for account icon in the search bar
 * @const 
 * */
 const ACCOUNT_ICON = '#root > div > .NavBar_navbar__2Ztou > .NavBar_container__1Z4JI > div:nth-child(4) > .NavBar_icons__2zmsz > span:nth-child(6) > svg '
/** 
  *  for settings icon in the dropdown menu when account icon is clicked
  * @const 
  * */
//  const EDIT_APPEARANCE_ICON = '#root > div > .NavBar_navbar__2Ztou > .NavBar_container__1Z4JI > div:nth-child(4) > .NavBar_icons__2zmsz > div:nth-child(9) > div > ul:nth-child(4) > a:nth-child(6)'
//  const EDIT_APPEARANCE_ICON = '#root > div > div > div > div:nth-child(4) > div > div:nth-child(9) > div > ul:nth-child(4) > a:nth-child(2)'
const EDIT_APPEARANCE_ICON = 'a[href="/customize"]'
 
//  const TITLE_TEXTBOX ="#root > div > div > div:nth-child(2) > ul:nth-child(2) > li > input"
const TITLE_TEXTBOX = 'input[id="t1"]' 
const DESCRIPTION_TEXTBOX = 'input[id="d1"]' 
const SAVE_BUTTON= '#root > div > div > div > button'
const HEADER_IMAGE_BUTTON = '#root > div > div > div:nth-child(2) > ul:nth-child(2) > li:nth-child(3) > div > div > label > svg > path'
const EXIT_BUTTON = "#root > div > div > div > a"
const AVATAR_SQUARE_BUTTON = 'input[value="square"]'
const AVATAR_CIRCLE_BUTTON = 'input[value="circle"]'
const CHANGE_BACKGROUND_COLOR_BUTTON = '#root > div > div > div:nth-child(2) > ul:nth-child(2) > li:nth-child(6) > div > input'
const CHANGE_TITLE_COLOR_BUTTON = '#root > div > div > div:nth-child(2) > ul:nth-child(2) > li:nth-child(7) > div > input'
const TOGGLE_HEADER_IMAGE = '#root > div > div > div:nth-child(2) > ul:nth-child(2) > li:nth-child(9) > div > span'

 /** 
  * var to hold the old password
  * 
  * @var */
   var password = '1234567menna'
   /** 
    * var to hold the email
    * @var */
   var email ='mennaahmedali77@gmail.com'

 /** @const */const CUSTOMIZE_VARIABLES = {
     ACCOUNT_ICON:ACCOUNT_ICON,
     EDIT_APPEARANCE_ICON:EDIT_APPEARANCE_ICON,
     email:email,
     password:password,
     TITLE_TEXTBOX:TITLE_TEXTBOX,
     SAVE_BUTTON:SAVE_BUTTON,
     DESCRIPTION_TEXTBOX:DESCRIPTION_TEXTBOX,
     HEADER_IMAGE_BUTTON:HEADER_IMAGE_BUTTON,
     EXIT_BUTTON:EXIT_BUTTON,
     AVATAR_CIRCLE_BUTTON:AVATAR_CIRCLE_BUTTON,
     AVATAR_SQUARE_BUTTON:AVATAR_SQUARE_BUTTON,
     CHANGE_BACKGROUND_COLOR_BUTTON:CHANGE_BACKGROUND_COLOR_BUTTON,
     CHANGE_TITLE_COLOR_BUTTON:CHANGE_TITLE_COLOR_BUTTON,
     TOGGLE_HEADER_IMAGE:TOGGLE_HEADER_IMAGE
     
     
 }
 module.exports={CUSTOMIZE_VARIABLES}