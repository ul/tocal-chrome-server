with import <nixpkgs> { };
mkShell {
  buildInputs = with python310Packages; [
    flask
    flask-cors
    pytz
    google-api-python-client
    google-auth-httplib2
    google-auth-oauthlib
  ];
}
