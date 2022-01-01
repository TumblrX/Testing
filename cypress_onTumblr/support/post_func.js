
import { POST_VARIABLES  } from './post_mapping_var';


/**
 * This function test get posts from the search bar account > posts,
 */

export function getPosts(){
    cy.get(POST_VARIABLES.ACCOUNT_ICON).click({multiple: true})
    cy.get(POST_VARIABLES.POSTS_PAGE).click({force: true})
}

/**
 * This function test find specific post by its id
 * @param {string}           postId post Id.
 * @param {string}           specificWord  Specific word in the post.
 */
 export function findPost(postId,specificWord){
    cy.get(POST_VARIABLES.POSTS_BLOCK + '> div[data-id="'+postId+'"]').contains(specificWord)

}
/**
 * This function test the count of posts
 * @param {number}           count posts count
 */
 export function countPosts(count){
    cy.get(POST_VARIABLES.POSTS_BLOCK).children() // get direct decendents 
    .should('have.length', count); // add assertion to have lenght of 5

}

/**
 * This function test delete a specific post by its id
 * @param {string}           postId post Id.

 */
 export function deletePost(postId){
    cy.get(POST_VARIABLES.POSTS_BLOCK + '> div[data-id="'+postId+'"] >'+POST_VARIABLES.DELETE_ICON).click()
    cy.get(POST_VARIABLES.CONFIRM_DELETE).click({force:true})

}
