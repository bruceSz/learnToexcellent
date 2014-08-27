function Ctrl2($scope) {
	var exprs = $scope.exprs = [];
	$scope.expr = '3*10|currency';
	$scope.addExp = function(expr) {
		exprs.push(expr);
	};

	$scope.removeExp = function(index) {
		exprs.splice(index,1);
	};
}

function Cntl1($window,$scope){
	$scope.name = 'World';
	$scope.greet = function() {
		($window.mockWindow||$window).alert('Hello' + $scope.name);
	}
}

function Controller() {
	$scope.master = {};

	$scope.update = function(user) {
		$scope.master = angular.copy(user);
	};

	$scope.reset = function() {
		$scope.user = angular.copy($scope.master);
	};
	$scope.reset();

}