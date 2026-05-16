import sys
from pathlib import Path
from unittest.mock import patch

import pytest

# Import the module to test
sys.path.insert(0, str(Path(__file__).parent.parent))

from dj_reframe.cli import USER_HOME_DIR


class TestOpenFileExplorer:
    """Tests for the open_file_explorer function"""

    @patch("dj_reframe.cli.subprocess.Popen")
    @patch("dj_reframe.cli.platform.system")
    @patch("dj_reframe.cli.Path.mkdir")
    def test_open_file_explorer_non_windows(self, mock_mkdir, mock_system, mock_popen):
        """Test file explorer opens correctly on macOS/Linux"""
        from dj_reframe.cli import open_file_explorer

        mock_system.return_value = "Darwin"

        test_path = Path("/test/path")
        open_file_explorer(test_path)

        mock_popen.assert_called_once_with(["open", test_path])

    @patch("dj_reframe.cli.subprocess.Popen")
    @patch("dj_reframe.cli.platform.system")
    @patch("dj_reframe.cli.Path.mkdir")
    def test_open_file_explorer_linux(self, mock_mkdir, mock_system, mock_popen):
        """Test file explorer opens correctly on Linux"""
        from dj_reframe.cli import open_file_explorer

        mock_system.return_value = "Linux"

        test_path = Path("/test/path")
        open_file_explorer(test_path)

        mock_popen.assert_called_once_with(["xdg-open", test_path])


class TestUserHomeDir:
    """Tests for USER_HOME_DIR configuration"""

    def test_user_home_dir_exists(self):
        """Test that USER_HOME_DIR is properly configured"""
        assert USER_HOME_DIR is not None
        assert USER_HOME_DIR.name == "my_templates"
        assert USER_HOME_DIR.parent.name == ".dj-reframe"

    def test_user_home_dir_is_path_object(self):
        """Test that USER_HOME_DIR is a Path object"""
        assert isinstance(USER_HOME_DIR, Path)


class TestMainFunction:
    """Tests for the main function"""

    @patch("dj_reframe.cli.argparse.ArgumentParser.parse_args")
    @patch("dj_reframe.cli.open_file_explorer")
    @patch("dj_reframe.cli.sys.exit")
    def test_main_with_my_templates_flag(self, mock_exit, mock_open, mock_args):
        """Test main function with --my-templates flag"""
        from dj_reframe.cli import main

        # Create a simple object with the required attributes
        args = type(
            "args", (), {"my_templates": True, "app_name": None, "app_type": None}
        )()
        mock_args.return_value = args

        # Make sys.exit actually exit by raising SystemExit
        mock_exit.side_effect = SystemExit(0)

        with pytest.raises(SystemExit) as exc_info:
            main()

        assert exc_info.value.code == 0
        mock_open.assert_called_once()
        mock_exit.assert_called_once_with(0)

    @patch("dj_reframe.cli.argparse.ArgumentParser.parse_args")
    @patch("dj_reframe.cli.argparse.ArgumentParser.print_help")
    @patch("dj_reframe.cli.sys.exit")
    def test_main_missing_args(self, mock_exit, mock_help, mock_args):
        """Test main function exits when missing required args"""
        from dj_reframe.cli import main

        # Create a simple object with the required attributes
        args = type(
            "args", (), {"my_templates": False, "app_name": None, "app_type": None}
        )()
        mock_args.return_value = args

        mock_exit.side_effect = SystemExit(1)

        with pytest.raises(SystemExit) as exc_info:
            main()

        assert exc_info.value.code == 1
        mock_help.assert_called_once()
        mock_exit.assert_called_once_with(1)

    @patch("dj_reframe.cli.argparse.ArgumentParser.parse_args")
    @patch("dj_reframe.cli.sys.exit")
    def test_main_hyphen_in_app_name(self, mock_exit, mock_args):
        """Test main function rejects app names with hyphens"""
        from dj_reframe.cli import main

        # Create a simple object with the required attributes
        args = type(
            "args",
            (),
            {"my_templates": False, "app_name": "my-app", "app_type": "site"},
        )()
        mock_args.return_value = args

        mock_exit.side_effect = SystemExit(1)

        with pytest.raises(SystemExit) as exc_info:
            main()

        assert exc_info.value.code == 1
        mock_exit.assert_called_once_with(1)
