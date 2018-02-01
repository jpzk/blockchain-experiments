pragma solidity ^0.4.17;

contract StoreValue {
  address public owner;
  string public data;

  event ValueChanged(string newValue); // Event
 
  function StoreValue() public {
      data = "";
  }

  function update(string newValue) public {
      data = newValue;
      ValueChanged(data);
  }
}