<?php
/* Authentification test, to include in every API file that needs authentication */

/* Sets HTTP Header in case of an anthentification fail and exits. */
function reject_auth()
{
    header('WWW-Authenticate: Basic');
    header('HTTP/1.0 401 Unauthorized');
    exit;
}

/* Checks for auth, to use in API pages for auth. */
function do_auth()
{
    if (!isset($_SERVER['PHP_AUTH_USER'])) {
        reject_auth();
    } else {
        $username = $_SERVER['PHP_AUTH_USER']; //username
        $pass_token = $_SERVER['PHP_AUTH_PW']; //hashed password
        
        
        // [ INSERER VERIFICATION DE L'IDENTITÉ DANS LA BASE DE DONNÉES ICI ]
        // Si pas ok, reject_auth()
        
        //Debug
        echo json_encode(array('user' => $username, 'pass' => $pass_token));
    }
}

//Debug
do_auth();

?>
