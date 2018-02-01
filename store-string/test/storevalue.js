var StoreValue = artifacts.require("StoreValue");

contract('StoreValue', function(accounts) {
    it("initialize with empty string", function() {
        return StoreValue.deployed()
        .then(function(instance) {
            return instance.data.call();
        })
        .then(function(value) {
            assert.equal(value.valueOf(), "", "String not empty on init.");
        });
    });
    it("should set a string", function() {
        return StoreValue.deployed()
        .then(function(instance) {
            meta = instance
            return meta.update("someval");
        })
        .then(function(returnVal) { 
            return meta.data.call();
        })
        .then(function(data) {
            assert.equal(data.valueOf(), "someval", "String should be someval after update.");
        })
    })
})