/// <reference types="cypress" />
/// <reference types="cypress-xpath" />

import{signIn} from'../../support/settings_func'
import{getPosts,findPost,deletePost,countPosts} from'../../support/post_func'

import { post_variables } from '../../support/post_mapping_var'

describe("Post Create Edit",function(){
    it("sign in",function(){

        signIn(post_variables.password,post_variables.email)
       
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

        findPost(post_variables.post_id,'second post')

    })
    //delete specific post
    it("delete post",function(){
     deletePost(post_variables.post_id)
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
