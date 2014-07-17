function Ctrl1($scope){
	$scope.name = 'angular';
}

function Ctrl2($scope) {
	$scope.format = 'M/d/yy h:mm:ss a';
}

angular.module('time',[]).directive('myCurrentTime',function($timeout,dateFilter){
	return function(scope,element,attrs){
		var format,
			timeoutId;

		function updateTime() {
			element.text(dateFilter(new Date(),format));
		}

		scope.$watch(attrs.myCurrentTime,function(value) {
			format = value;
			updateTime();
		});

		function updateLater() {
			timeoutId = $timeout(function(){
				updateTime();
				updateLater();
			},1000);
		}

		element.bind('$destroy',function(){
			$timeout.cancel(timeoutId);
		});
		updateLater();

	}
});