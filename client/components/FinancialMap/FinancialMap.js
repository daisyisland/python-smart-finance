Template.FinancialMap.onCreated(function(){
	var self = this;
	self.autorun(function (){
		self.subscribe('recipes');
	});
});

Template.FinancialMap.helpers({
	recipes: ()=> {
		return Recipes.find({inMenu: true});
	}
});