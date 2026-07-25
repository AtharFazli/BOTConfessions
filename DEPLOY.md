# Deploy BOTConfessions to Mainnet

## 1. Deploy Contract

BOTConfessions.sol — compile with Solidity ^0.8.20 on Remix or local tool.

On-chain methods needed:
- `postConfession(string)` payable 0.001 BOT
- `heart(uint256)` payable 0.001 BOT
- `getCount()` view
- `confessions(uint256)` view (auto-generated getter for public array)
- `hasHearted(uint256,address)` view
- `withdraw()` onlyOwner

Bytecode already verified on testnet (same source).

**Easiest:** open [Remix](https://remix.ethereum.org), paste `BOTConfessions.sol`, compile, deploy via Injected Web3 with MetaMask on **BOT Chain (chain 677)**.

Network config:
- RPC: https://rpc.botchain.ai
- Chain ID: 677
- Symbol: BOT
- Explorer: https://scan.botchain.ai

## 2. Update Frontend

Edit `index.html`:

1. **Line 91** — ganti CONTRACT address ke address hasil deploy
2. **Line 98** — aktifin mainnet:
   ```js
   const CHAIN = MAINNET_CHAIN;
   // const CHAIN = TESTNET_CHAIN;
   ```
3. **Line 102** — set `HAS_RANGE = true` (krn contract baru punya `getConfessionsRange`)

## 3. Verify

- Buka fazly.web.id
- Connect wallet → switch ke BOT Chain mainnet
- Cek confession list muncul dari contract baru
- Test post + heart

## Post-Deploy Checklist

- [ ] Contract deployed on chain 677
- [ ] CONTRACT address updated
- [ ] CHAIN = MAINNET_CHAIN
- [ ] HAS_RANGE = true
- [ ] Site loads confessions from mainnet
