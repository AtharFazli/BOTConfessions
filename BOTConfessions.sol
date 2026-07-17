// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract BOTConfessions {
    struct Confession {
        address author;
        string message;
        uint256 timestamp;
        uint256 hearts;
    }

    Confession[] public confessions;
    uint256 public constant POST_PRICE = 0.001 ether;
    uint256 public constant HEART_PRICE = 0.001 ether;

    event NewConfession(uint256 indexed id, address indexed author);
    event HeartAdded(uint256 indexed id, address indexed from);

    function postConfession(string calldata _message) external payable {
        require(msg.value >= POST_PRICE, "Need 0.001 tBOT");
        confessions.push(Confession(msg.sender, _message, block.timestamp, 0));
        emit NewConfession(confessions.length - 1, msg.sender);
    }

    function heart(uint256 _id) external payable {
        require(_id < confessions.length, "Not found");
        require(msg.value >= HEART_PRICE, "Need 0.001 tBOT");
        confessions[_id].hearts++;
        emit HeartAdded(_id, msg.sender);
    }

    function getConfessions() external view returns (Confession[] memory) {
        return confessions;
    }

    function getCount() external view returns (uint256) {
        return confessions.length;
    }
}
