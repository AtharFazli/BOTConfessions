# BOTConfessions

Anonymous on-chain confession board for BOTChain.

## How it works
- Post a confession — 0.001 tBOT
- Heart a confession — 0.001 tBOT
- All data stored on-chain, immutable

## Files
- `BOTConfessions.sol` — smart contract (Solidity 0.8.20)
- `index.html` — frontend (connect MetaMask + post/heart)

## Deploy
1. Remix → compile `BOTConfessions.sol` (v0.8.20)
2. Deploy to BOT Chain Testnet (Chain ID 968, RPC: https://rpc.bohr.life)
3. Copy contract address → paste into `index.html` line `const CONTRACT = "0x..."`
4. Host `index.html` on GitHub Pages + custom domain
