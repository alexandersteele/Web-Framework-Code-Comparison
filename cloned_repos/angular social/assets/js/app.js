myApp = angular.module('rekonnect', ['ui.router', 'ngResource']); //Module and resources


/*Configurations*/
myApp.config(function ($stateProvider, $urlRouterProvider) {
    //Routing for feed page
    $stateProvider
        .state('feed', {
            url: '/feed',
            templateUrl: 'assets/partials/feed.html',
            controller: 'FeedController'
        })
        //Routing for secure page
        .state('secure', {
            url: '/secure',
            templateUrl: 'assets/partials/secure.html',
            controller: 'SecureController'
        });
    $urlRouterProvider.otherwise('/feed'); //Default page set to feed
});


/*Feed page controller*/
myApp.controller("FeedController", function ($scope, api) {
    //Get viral photos for feed page
    feed_response = api.get_viral_photos()
    feed_response.$promise.then(function onSuccess(data) { //If response from api call is success
        // Access data from 'response'
        $scope.viral_photos = data.data; //Make visible to HTML
    },
    function onFail(data) { //If response from api call is failure
        console.error("Failed to get response from API");
    });
});


/*Secure page controller*/
myApp.controller("SecureController", function ($scope, api) {
    //Login button authorization redirection
    $scope.login = function () {
        window.location.href = "https://api.imgur.com/oauth2/authorize?client_id=e8728581f97f521&response_type=token"
    }
    
    $scope.accessToken = JSON.parse(window.localStorage.getItem("imgur")).oauth.access_token; //Access token visible from HTML
    $scope.username = JSON.parse(window.localStorage.getItem("imgur")).oauth.account_username; //Username visible from HTML
    
    //Get photos from user
    photo_response = api.get_photos()
    photo_response.$promise.then(function onSuccess(data) { //If response from api call is success
        // Access data from 'response'
        $scope.photos = data.data; //Make visible to HTML
    },
    function onFail(data) { //If response from api call is failure
        console.error("Failed to get response from API");
    });
    
    //Get comments from user
    comment_response = api.get_comments()
    comment_response.$promise.then(function onSuccess(data) { //If response from api call is success
            // Access data from 'response'
            $scope.comments = data.data; //Make visible to HTML
        },
        function onFail(data) { //If response from api call is failure
            console.error("Failed to get response from API");
        });

});





























/*Factory API function*/
myApp.factory('api', function ($resource) {

    accessToken = JSON.parse(window.localStorage.getItem("imgur")).oauth.access_token; //Use oauth to get access token
    username = JSON.parse(window.localStorage.getItem("imgur")).oauth.account_username; //Use oauth to get username
    
    //Factory user photo get resource
    var photos = $resource('https://api.imgur.com/3/account/' + username + '/images/', {}, {
        get: {
            method: 'GET',
            headers: {
                'Authorization': 'Bearer ' + accessToken //Header authorization with access token
            }
        }
    });
    
    //Factory feed photo getter resource (set by default to cat gallery to avoid MP4 files not rendering on viral feed)
    var viral_photos = $resource('https://api.imgur.com/3/gallery/7rHtr/images/?client_id=e8728581f97f521');

    //Factory comments get resource
    var comments = $resource('https://api.imgur.com/3/account/' + username + '/comments/', {}, {
        get: {
            method: 'GET',
            headers: {
                'Authorization': 'Bearer ' + accessToken //Header authorization with access token
            }
        }
    });
    
    //Factory resource return functions 
    return {
        get_photos: function (success, error) {
            return photos.get();
        },
        get_viral_photos: function (success, error) {
            return viral_photos.get();
        },
        get_comments: function (success, error) {
            return comments.get();
        }
    };
});
