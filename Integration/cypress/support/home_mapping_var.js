/** 
 *  for account icon in the search bar
 * @const 
 * */
 const ACCOUNT_ICON = '#root > div > .NavBar_navbar__2Ztou > .NavBar_container__1Z4JI > div:nth-child(4) > .NavBar_icons__2zmsz > span:nth-child(6) > svg '
 const AVATAR_PAGE_ICON = '#root > div > div > div > div:nth-child(4) > div > div:nth-child(9) > div > ul:nth-child(4) > a'
 const LOGIN_WITH_EMAIL_BUTTON = '#root > .MainPage_bodyMainPage__2bmsj > .MainPage_container__3VWBn > .MainPage_content__3Ccvh > .MainPage_buttonWrapper__1Oxaq > .MainPage_login__27tt_'
 const INPUT_EMAIL = 'input[name="email"]'
 const INPUT_PASSWORD ='input[name="password"]'
 const LOGIN_BUTTON ='input[id="login"]'
 const CREATE_POST_BUTTON ='#root > div:nth-child(2) > div > div:nth-child(2) > div > div > div:nth-child(2) > div > a > svg'
 const POST_TITLE_TEXTBOX ='#root > div > div > div:nth-child(2) > form > input'
 const POST_TEXT_TEXTBOX ='#root > div > div > div:nth-child(2) > form > div > div:nth-child(2)'
 const POST_BUTTON='#root > div > div > div:nth-child(2) > form > div:nth-child(4) > div:nth-child(2) > button'
 const CHECK_ADDED_POST = '#root > div:nth-child(2) > div > div:nth-child(2) > div > div:nth-child(2) > div:nth-child(2) > div'
 const ADDED_POST_P = CHECK_ADDED_POST + ' > div:nth-child(2) > p'
 const DELETE_POST_BUTTON='#root > div:nth-child(2) > div > div > div:nth-child(3) > div > div > div > div > footer > div:nth-child(2) > div:nth-child(4) > svg'
 const LIKE_POST_BUTTON='#root > div:nth-child(2) > div > div:nth-child(2) > div > div:nth-child(2) > div:nth-child(2) > div > footer > div:nth-child(2) > div:nth-child(3)'
 const CHECK_LIKE_ADDED ='#root > div:nth-child(2) > div > div:nth-child(2) > div > div:nth-child(2) > div:nth-child(2) > div > footer > div'
 const ADD_COMMENT_BUTTON ='#root > div:nth-child(2) > div > div:nth-child(2) > div > div:nth-child(2) > div:nth-child(2) > div > footer > div:nth-child(2) > div:nth-child(1) > svg'
 const REPLY_TEXTBOX ='#root > div:nth-child(2) > div > div:nth-child(2) > div > div:nth-child(2) > div:nth-child(2) > div > footer > div:nth-child(2) > div > div:nth-child(2) > footer > form > input'
 const REPLY_BUTTON = '#root > div:nth-child(2) > div > div:nth-child(2) > div > div:nth-child(2) > div:nth-child(2) > div > footer > div:nth-child(2) > div > div:nth-child(2) > footer > form > button'
 const REPLY_BACK_BUTTON ='#root > div:nth-child(2) > div > div:nth-child(2) > div > div:nth-child(2) > div:nth-child(2) > div > footer > div > div > div:nth-child(2) > Header > div > svg'
 const SEARCH_TEXT='input[id="myText"]'
 const CREATE_LINK_BUTTON ='#root > div:nth-child(2) > div > div > div > div > div:nth-child(2) > div > a:nth-child(4)'
 const INSERT_LINK_BUTTON = '#root > div > div > div:nth-child(2) > form > div:nth-child(2) > div > div:nth-child(4) > div:nth-child(1) > img'
 const LINK_TITLE ='input[id="linkTitle"]'
 const LINK_TARGET ='input[id="linkTarget"]'
 const ADD_BUTTON = '#root > div > div > div:nth-child(2) > form > div:nth-child(2) > div > div:nth-child(4) > div:nth-child(3) > span:nth-child(6) > button'
 const REBLOG_BUTTON='[data-test-id="testPost2"]'
 const PRE_REBLOG_BUTTON='#root > div:nth-child(2) > div > div > div > div:nth-child(5) > div:nth-child(2) > div:nth-child(1) > footer > div:nth-child(2) > div:nth-child(2) > svg'
 const POST_REBLOG_BUTTON='div:nth-child(2) > div > footer > div:nth-child(2) > div:nth-child(2) > svg'
 /** 
  * var to hold the old password
  * 
  * @var */
   var password = '1234567menna'
   /** 
    * var to hold the email
    * @var */
   var email ='mennaahmedali77@gmail.com'

 /** @const */const HOME_VARIABLES = {
     password:password,
     email:email,
     ACCOUNT_ICON:ACCOUNT_ICON,
     CREATE_POST_BUTTON:CREATE_POST_BUTTON,
     POST_TITLE_TEXTBOX:POST_TITLE_TEXTBOX,
     POST_TEXT_TEXTBOX:POST_TEXT_TEXTBOX,
     POST_BUTTON:POST_BUTTON,
     CHECK_ADDED_POST:CHECK_ADDED_POST,
     ADDED_POST_P:ADDED_POST_P,
     DELETE_POST_BUTTON:DELETE_POST_BUTTON,
     LIKE_POST_BUTTON:LIKE_POST_BUTTON,
     CHECK_LIKE_ADDED:CHECK_LIKE_ADDED,
     ADD_COMMENT_BUTTON:ADD_COMMENT_BUTTON,
     REPLY_TEXTBOX:REPLY_TEXTBOX,
     REPLY_BUTTON:REPLY_BUTTON,
     REPLY_BACK_BUTTON:REPLY_BACK_BUTTON,
     INPUT_EMAIL:INPUT_EMAIL,
     INPUT_PASSWORD:INPUT_PASSWORD,
     LOGIN_BUTTON:LOGIN_BUTTON,
     LOGIN_WITH_EMAIL_BUTTON:LOGIN_WITH_EMAIL_BUTTON,
     AVATAR_PAGE_ICON:AVATAR_PAGE_ICON,
     SEARCH_TEXT:SEARCH_TEXT,
     CREATE_LINK_BUTTON:CREATE_LINK_BUTTON,
     INSERT_LINK_BUTTON:INSERT_LINK_BUTTON,
     LINK_TITLE:LINK_TITLE,
     LINK_TARGET:LINK_TARGET,
     ADD_BUTTON:ADD_BUTTON,
     REBLOG_BUTTON:REBLOG_BUTTON,
     REBLOG_BUTTON:REBLOG_BUTTON,
     PRE_REBLOG_BUTTON:PRE_REBLOG_BUTTON,
     POST_REBLOG_BUTTON:POST_REBLOG_BUTTON
     
 }
 module.exports={HOME_VARIABLES}