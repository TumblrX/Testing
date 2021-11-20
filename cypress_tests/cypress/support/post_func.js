
import { post_variables  } from './post_mapping_var';


/**
 * This fnction test get posts from the search bar account > posts 
 */

export function getPosts(){
    cy.get(post_variables.account_icon).click({multiple: true})
    cy.get(post_variables.posts_page).click({force: true})
}

/**
 * This function test find specific post by its id
 * @param {string}           postId post Id.
 * @param {string}           specificWord  Specific word in the post.
 */
 export function findPost(postId,specificWord){
    cy.get(post_variables.posts_block + '> div[data-id="'+postId+'"]').contains(specificWord)

}
/**
 * This function test the count of posts
 * @param {number}           count posts count
 */
 export function countPosts(count){
    cy.get(post_variables.posts_block).children() // get direct decendents 
    .should('have.length', count); // add assertion to have lenght of 5

}

/**
 * This function test delete a specific post by its id
 * @param {string}           postId post Id.

 */
 export function deletePost(postId){
    cy.get(post_variables.posts_block + '> div[data-id="'+postId+'"] >'+post_variables.delete_icon).click()
    cy.get(post_variables.confirm_delete).click({force:true})

}
