# BOTConfessions

Anonymous on-chain confession board for BOTChain. Built for **GMT Build Week Hackathon**.

## DApp Overview

- **Post** a confession — 0.001 tBOT
- **Heart** a confession — 0.001 tBOT (max 1 per user per post)
- No author stored on-chain — truly anonymous
- Random ID instead of sequential (privacy)
- Connect MetaMask, no backend needed

## Status

✅ Contract deployed at **`0x2983b7A9BE9EACE315a0cf6A368FA3D8DDb787F3`** (OLD — v1 with author)
🔄 **REDEPLOY REQUESTED** — v2 (no author, random ID, 1 heart per user)

### 1. Redeploy Contract

1. Go to [remix.ethereum.org](https://remix.ethereum.org)
2. Open `BOTConfessions.sol` (paste the new version)
3. Compiler → v0.8.20 → Compile
4. Deploy → Environment: `Injected Provider - MetaMask` → Deploy
5. Copy deployed contract address
6. Update it in `index.html` (search `PASTE_DEPLOYED_ADDRESS_HERE`)

### 2. MetaMask Setup
- Add network: **BOT Chain Testnet**
  - Name: `BOT Chain Testnet`
  - RPC: `https://rpc.bohr.life`
  - Chain ID: `968`
  - Symbol: `tBOT`

### 3. Get Test Tokens
- Ask organizer or BOT Chain Discord faucet for free tBOT (testnet, no real value)

### 4. Deploy to Web
- Push to GitHub — auto-deploys to GitHub Pages
- Custom domain: `fazly.web.id`

### 5. Submission (due Aug 4, 11:59 PM)
Submit all 4:
  1. Deployed contract address
  2. Live website URL: `https://fazly.web.id`
  3. GitHub repo: `https://github.com/AtharFazli/BOTConfessions`
  4. Demo video (2-3 min, show connect wallet → post → heart)

## Judging Criteria
| Item | Points |
|------|--------|
| Contract deployed & working | 30 |
| Anyone can connect & use | 25 |
| Unique wallets interacted | 20 |
| Use case originality | 15 |
| Demo video quality | 10 |
| **Total** | **100** |

## Files
- `BOTConfessions.sol` — Solidity contract (v0.8.20)
- `index.html` — Web3 frontend (dark theme)
