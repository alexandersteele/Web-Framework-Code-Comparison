var myApp = angular.module("myApp", ['ngRoute', 'ngSanitize', 'ngResource', 'mgcrea.ngStrap']);

//Application controller assignment and routing
myApp.config(function ($routeProvider, $locationProvider) {
    $routeProvider.when('/', {
        controller: 'indexCtrl',
        templateUrl: '/partials/index.html'
    });

    $routeProvider.when('/task/:id', {
        controller: 'taskCtrl',
        templateUrl: '/partials/task.html'
    });

    $routeProvider.when('/add-task', {
        controller: 'addTaskCtrl',
        templateUrl: '/partials/add.html'
    });

    $locationProvider.html5Mode({
        enabled: true,
        requireBase: false
    });

})


//Search Tool Controller
myApp.controller('appCtrl', function ($scope, $location) {
    //Redirect to homepage on keypress
    $scope.startSearch = function () {
        $location.path('/');
    };
});


//Index Controller
myApp.controller('indexCtrl', function ($scope, tasks, $alert) {
    
    //Get tasks to display
    $scope.tasks = tasks.get();
    
    //Delete task
    $scope.delete = function(index){
      tasks.destroy($scope.tasks[index].id);
      $scope.tasks.splice(index, 1);
      
  };

});


//Task Controller
myApp.controller('taskCtrl', function ($scope, $routeParams, tasks, $timeout) {
    var response = tasks.find($routeParams.id)
    response.$promise.then(function onSuccess(data) {
            // access data from 'response'
            $scope.task = data[0];
        },
        function onFail(data) {
            // handle failure
        });
    
    //Update on task edit
    $scope.$on('saved', function () {
        $timeout(function () {
            $scope.task.$update();
        }, 0);
    });

});


//Add Task Controller
myApp.controller('addTaskCtrl', function ($scope, tasks) {
    //When task is added
    $scope.submit = function () {
        $scope.task.$save();
        $scope.task = tasks.create();
        $scope.added = true;
    };

    $scope.task = tasks.create();
});


//Tasks Factory Controller for Task CRUD
myApp.factory('tasks', function ($resource) {
    
    var resource = $resource('http://localhost:5000/tasks/:id', {
        id: '@id'
    }, {
        update: {
            method: 'PUT'
        }
    });
    return {
        get: function () {
            return resource.query();
        },
        find: function (id) {
            return $resource('http://localhost:5000/task/:id').query({
                id: id
            });
        },
        create: function () {
            return new resource();
        },
        destroy: function (id) {
            $resource('http://localhost:5000/task/:id').delete({
                id: id
            });
        }
    };


})

//Task Edit Directive Functionality
myApp.directive('editable', function () {
    return {
        restrict: 'A',
        templateUrl: '/partials/editable.html',
        scope: {
            value: '=editable',
            field: '@fieldType'
        },
        controller: function ($scope, tasks) {
            $scope.editor = {
                showing: false,
                value: $scope.value
            };
            
            //Toggle edit task
            $scope.toggleEditor = function () {
                $scope.editor.showing = !$scope.editor.showing;
            };
            
            //Check field is text
            $scope.field = ($scope.field) ? $scope.field : 'text';
            
            //Emit saved changes to Task Controller
            $scope.save = function () {
                $scope.value = $scope.editor.value;
                $scope.toggleEditor();
                $scope.$emit('saved');
            };


        }
    };
})
