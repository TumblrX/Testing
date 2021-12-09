/// <reference types="cypress" />
/// <reference types="cypress-xpath" />

import{signIn} from'../../support/settings_func'
import{getPosts,findPost,deletePost,countPosts} from'../../support/post_func'

import { POST_VARIABLES } from '../../support/post_mapping_var'

describe("Post Create Edit",function(){
    it("sign in",function(){

        signIn(POST_VARIABLES.password,POST_VARIABLES.email)
       
    })
    // Go to posts from the search bar icon
    it("get posts",function(){

        getPosts()
        
    })
    // Go posts count
    it("count posts",function(){

        countPosts(2)
        
    })
    //find specific post
    it("Find post",function(){

        findPost(POST_VARIABLES.POST_ID,'second post')

    })
    //delete specific post
    it("delete post",function(){
     deletePost(POST_VARIABLES.POST_ID)
     countPosts(1)
    })

    // Create a post 
    // it("Create Text post",function(){
     
    //     var text_icon = '#root > #base-container > .D5eCV > .gPQR5 > .lSyOz > .O4V_R > div:nth-child(3) > ul:nth-child(2) > li:nth-child(1) > button:nth-child(1)';
    //     cy.get(text_icon).click({force: true});
    //     cy.get('.vP3g8').then(($iframe) => {
    //         const $body = $iframe.contents().find('body')
    //         const $win = $iframe[0].contentWindow

    //       cy.stub($win.console, 'log').as('consoleLog')

      
    //       cy.wrap($body)
    //         .find('p').type('test')
    //     })
    //   })

})
