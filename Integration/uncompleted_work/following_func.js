
import { VARIABLES } from './following_mapping_var';

/**
 * this function check following
 */
export function checkFollowing() {
    cy.wait(20)
    var name = cy.get(VARIABLES.FOLLOWING_BOX).find('div').eq(1).invoke('text').then((txt) => {
       return txt
    })
    console.log('the name is : ' + name)
    cy.get(VARIABLES.FOLLOWING_BOX).find('div').eq(2).click()
    cy.visit('http://tumblrx.me:4000/following')

    cy.get(VARIABLES.FOLLOWING_SEARCH_BAR).type(toString(name))
    cy.get(VARIABLES.SEARCH_ERROR).should('contain', name)
    // var flage = false
    // var num
    // cy.get(VARIABLES.NUM_OF_FOLLOWERS).invoke('Text').then((txt) => {
    //     num = parseInt(txt)
    //     console.log('the num is : ' + num + ' ' + txt)
    // })
    // var i = 0
    // while(cy.get(VARIABLES.FOLLOWING_LIST).find('div').eq(i) != cy.get(VARIABLES.FOLLOWING_LIST).find('div').eq(-1)){
    //     var ishere
    //     cy.get(VARIABLES.FOLLOWING_LIST).find('div').eq(i).invoke('text').then((txt) => {
    //         ishere = txt
    //         console.log('the name is : ' + ishere)
    //     })
    //     if(ishere == name){
    //         flage = true
    //     }
    //     i++
    // }
}

