pragma solidity ^0.8.0;

contract MalkhanaManagementSystem {
    struct Item {
        string barcode;
        string itemName;
        string checkInTime;
        string checkOutTime;
    }
    
    mapping(string => Item) private malkhanaTable;
    mapping(string => Item) private forensicLabTable;
    
    event ItemCheckedIn(string barcode, string itemName, string checkInTime);
    event ItemCheckedOut(string barcode, string checkOutTime);
    
    function checkInItem(string memory barcode, string memory itemName) public {
        require(bytes(barcode).length > 0, "Barcode cannot be empty");
        require(bytes(itemName).length > 0, "Item name cannot be empty");
        require(bytes(malkhanaTable[barcode].barcode).length == 0, "Item with the same barcode already checked in");
        
        Item memory newItem = Item(barcode, itemName, getCurrentTime(), "");
        malkhanaTable[barcode] = newItem;
        
        emit ItemCheckedIn(barcode, itemName, newItem.checkInTime);
    }
    
    function checkOutItem(string memory barcode) public {
        require(bytes(barcode).length > 0, "Barcode cannot be empty");
        require(bytes(malkhanaTable[barcode].barcode).length > 0, "Item with the given barcode not found");
        require(bytes(malkhanaTable[barcode].checkOutTime).length == 0, "Item with the given barcode already checked out");
        
        Item storage checkedOutItem = malkhanaTable[barcode];
        checkedOutItem.checkOutTime = getCurrentTime();
        
        forensicLabTable[barcode] = checkedOutItem;
        delete malkhanaTable[barcode];
        
        emit ItemCheckedOut(barcode, checkedOutItem.checkOutTime);
    }
    
    function getMalkhanaItem(string memory barcode) public view returns (Item memory) {
        return malkhanaTable[barcode];
    }
    
    function getForensicLabItem(string memory barcode) public view returns (Item memory) {
        return forensicLabTable[barcode];
    }
    
    function getCurrentTime() private view returns (string memory) {
        return string(abi.encodePacked(block.timestamp));
    }
}
