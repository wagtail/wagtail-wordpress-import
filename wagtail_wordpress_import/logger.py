import csv
import sys
from datetime import datetime


class Logger:
    def __init__(self, logdir):
        self.logdir = logdir
        self.processed = 0
        self.imported = 0
        self.skipped = 0
        self.items = []
        self.images = []
        self.urls = []
        self.page_link_errors = []

    def log_progress(self):
        item = self.items[-1]
        if not item["id"] == 0:
            sys.stdout.write(
                f"Wagtail ID: {item['id']}, {item['title']}, {item['result']}\n"
            )

    def get_items_report_data(self):
        report_data = {
            "processed": self.processed,
            "imported": self.imported,
            "skipped": self.skipped,
            "items": self.items,
        }

        return report_data

    def output_import_summary(self):
        sys.stdout.write("Summary ========================")
        sys.stdout.write(
            "\nImported: "
            + str(self.imported)
            + " Skipped: "
            + str(self.skipped)
            + " Processed: "
            + str(self.processed)
        )
        if self.processed - self.skipped == self.imported:
            sys.stdout.write("\n✅ Completed Successfully\n")
        else:
            sys.stdout.write(
                "\n⚠️ Completed but there were errors with imported amounts\n"
            )

    def save_csv_import_report(self):
        self._write_csv(
            "import-report",
            self.items,
            ["id", "title", "url", "reason", "result", "dates", "slug"],
            {
                "id": "Page ID",
                "title": "Page Title",
                "url": "Wordpress Link",
                "reason": "Reason for result ->",
                "result": "Result",
                "dates": "Dates Changed",
                "slug": "Slug Changed",
            },
            row_map=lambda row: {
                "id": row["id"],
                "title": row["title"],
                "url": row["link"],
                "reason": row["reason"],
                "result": row["result"],
                "dates": row["datecheck"],
                "slug": row["slugcheck"],
            },
        )

    def save_csv_images_report(self):
        self._write_csv(
            "images-report",
            self.images,
            ["id", "title", "url", "reason"],
            {
                "id": "Page ID",
                "title": "Page Title",
                "url": "Wordpress Link",
                "reason": "Reason",
            },
            row_map=lambda row: {
                "id": row["id"],
                "title": row["title"],
                "url": row["link"],
                "reason": row["reason"],
            },
        )

    def save_csv_pagelink_errors_report(self):
        # self.page_link_errors is a list of tuples (link, page_object)
        data = [
            {"id": page.id, "title": page.title, "link": link}
            for link, page in self.page_link_errors
        ]
        self._write_csv(
            "pagelink_errors-report",
            data,
            ["id", "title", "link"],
            {"id": "Page ID", "title": "Page Title", "link": "Wordpress Link"},
        )

    def _write_csv(self, file_suffix, data, fieldnames, header_mapping, row_map=None):
        file_name = f"{self.logdir}/{file_suffix}-{datetime.now().strftime('%Y%m%d-%H%M%S')}.csv"
        
        with open(file_name, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(header_mapping)
            for item in data:
                row = row_map(item) if row_map else item
                writer.writerow(row)
