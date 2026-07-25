# BOTConfessions

Anonymous on-chain confession board for BOTChain. Built for **GMT Build Week Hackathon**.

## DApp Overview

- **Post** a confession — 0.001 tBOT
- **Heart** a confession — 0.001 tBOT (max 1 per user per post)
- No author stored on-chain — truly anonymous
- Random ID instead of sequential (privacy)
- Connect MetaMask, no backend needed

## MetaMask Setup
- Add network: **BOT Chain Testnet**
  - Name: `BOT Chain Testnet`
  - RPC: `https://rpc.bohr.life`
  - Chain ID: `968`
  - Symbol: `tBOT`

## Live
- **Contract**: `0x04e6db5BE9861fbEd3E7a4192A3444a7D0e07cb4` (v2, no author)
- **Website**: `https://fazly.web.id`
- **Repo**: `https://github.com/AtharFazli/BOTConfessions`

## Submission (due Aug 4, 11:59 PM)
Submit all 4:
  1. Deployed contract address: `0x04e6db5BE9861fbEd3E7a4192A3444a7D0e07cb4`
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
