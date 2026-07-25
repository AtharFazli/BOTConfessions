// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract BOTConfessions {
    struct Confession {
        uint256 id;
        string message;
        uint256 hearts;
    }

    Confession[] public confessions;
    uint256 public constant POST_PRICE = 0.001 ether;
    uint256 public constant HEART_PRICE = 0.001 ether;
    uint256 public constant MAX_LENGTH = 500;

    address public owner;

    mapping(uint256 => mapping(address => bool)) public hasHearted;

    event NewConfession(uint256 indexed id, uint256 indexed arrayIndex);
    event HeartAdded(uint256 indexed arrayIndex, address indexed from);

    modifier onlyOwner() {
        require(msg.sender == owner, "Not owner");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    function postConfession(string calldata _message) external payable {
        require(msg.value >= POST_PRICE, "Need 0.001 BOT");
        require(bytes(_message).length > 0, "Empty message");
        require(bytes(_message).length <= MAX_LENGTH, "Max 500 chars");
        uint256 id = uint256(
            keccak256(abi.encodePacked(block.timestamp, msg.sender, block.prevrandao, confessions.length))
        );
        confessions.push(Confession(id, _message, 0));
        emit NewConfession(id, confessions.length - 1);
    }

    function heart(uint256 _index) external payable {
        require(_index < confessions.length, "Not found");
        require(msg.value >= HEART_PRICE, "Need 0.001 BOT");
        require(!hasHearted[_index][msg.sender], "Already hearted");
        hasHearted[_index][msg.sender] = true;
        confessions[_index].hearts++;
        emit HeartAdded(_index, msg.sender);
    }

    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds");
        (bool sent, ) = payable(owner).call{value: balance}("");
        require(sent, "Withdraw failed");
    }

    function getConfessions() external view returns (Confession[] memory) {
        return confessions;
    }

    function getConfessionsRange(uint256 start, uint256 count) external view returns (Confession[] memory) {
        if (start >= confessions.length) return new Confession[](0);
        uint256 end = start + count;
        if (end > confessions.length) end = confessions.length;
        Confession[] memory result = new Confession[](end - start);
        for (uint256 i = start; i < end; i++) {
            result[i - start] = confessions[i];
        }
        return result;
    }

    function getCount() external view returns (uint256) {
        return confessions.length;
    }
}
