var App = angular.module("App", ["ionic"]);

App.controller("AppCtrl", ["Scope", "$log", AppCtrl]);

function AppCtrl(Scope, $log) {
    $scope.refresh = function() {
        document.getElementById("title").style.color = "red";
    }
}