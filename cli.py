import argparse
import sys
import utils
import click

@click.command()
@click.option("--pdf_name",prompt=True)

def test(pdf_name):
    text_file_name=utils.convert_pdf_to_text(pdf_name)
    utils.text_to_audio(text_file_name)
    sys.stdout.write('created')


if __name__ == "__main__":
    test('')