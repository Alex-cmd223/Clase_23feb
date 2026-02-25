{ pkgs, ... }: {
  channel = "stable-23.11";
  packages = [
    pkgs.python311
    pkgs.python311Packages.pip
    pkgs.python311Packages.flask
    pkgs.python311Packages.flask-cors
  ];
  idx = {
    extensions = [
      "ms-python.python"
      "ms-python.vscode-pylance"
    ];
  };
}