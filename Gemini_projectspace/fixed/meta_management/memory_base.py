import os
import json
from datetime import datetime, timezone
import fcntl # Linux/Mac環境でのファイルロック用

class BaseMemoryLayer:
    """記憶レイヤーの共通ベースクラス。Registryへの安全なアクセスを提供する。"""
    def __init__(self, workspace_root):
        self.workspace_root = workspace_root
        self.registry_path = os.path.join(workspace_root, "meta_management/registry.json")

    def _get_utc_now(self):
        """タイムゾーン付きのISOフォーマット(Z付き)を返す"""
        return datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')

    def update_registry(self, update_func):
        """
        Registryを安全に読み込み、更新関数を適用して保存する。
        ファイルロックを使用して並行処理時の競合を防ぐ。
        """
        if not os.path.exists(self.registry_path):
            print(f"Registry not found at {self.registry_path}. Skipping update.")
            return

        with open(self.registry_path, 'r+') as f:
            # 他のプロセスが書き込まないようにロック
            fcntl.flock(f, fcntl.LOCK_EX)
            try:
                data = json.load(f)
                
                # サブクラスから渡された関数でデータを更新
                updated_data = update_func(data)
                updated_data["last_updated"] = self._get_utc_now()
                
                # ファイルの先頭に戻って上書き
                f.seek(0)
                json.dump(updated_data, f, indent=2)
                f.truncate()
            except json.JSONDecodeError:
                print("Error: registry.json is corrupted.")
            finally:
                # ロックを解除
                fcntl.flock(f, fcntl.LOCK_UN)